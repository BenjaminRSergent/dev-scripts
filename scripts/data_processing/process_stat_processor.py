import sys
import os
import subprocess
import time
from enum import Enum
import matplotlib.pyplot as plt

STOP_RECORDING_FILE = "./.stop_recording"

class process_info:
    class StatType(Enum):
        ARGS = 0
        PID = 1
        CPU = 2
        MEMORY = 3

    stat_to_arg = {StatType.ARGS : "args", StatType.PID : "pid", StatType.CPU : r"%cpu", StatType.MEMORY : r"%mem"}

    def __init__(self, stat_list, stat_order,cpu_freqs):
        #Args must be the final command for now because it can include spaces that
        # break parsing
        assert not process_info.StatType.ARGS in stat_list or stat_list[-1] == process_info.StatType.ARGS

        self.stat_map = {}
        for (index,stat_type) in enumerate(stat_order):
            if(stat_type == process_info.StatType.ARGS):
                args = stat_list[index:]
                self.name = args[0]
                self.command = "".join(args)
                self.stat_map[stat_type] = args[1:]
            elif(stat_type == process_info.StatType.CPU):
                self.raw_cpu_percent = float(stat_list[index])
                self.stat_map[stat_type] = self.raw_cpu_percent*sum(cpu_freqs)
            else:
                self.stat_map[stat_type] = stat_list[index]


    def get_name(self):
        return self.name

    def get_raw_cpu(self):
        return self.raw_cpu_percent

    def get_stat(self, stat_type):
        return self.stat_map[stat_type]

    def get_ps_command_for(stat_order):
        #Args must be the final command for now because it can include spaces
        #break parsing
        assert not process_info.StatType.ARGS in stat_order or stat_order[-1] == process_info.StatType.ARGS
        command = "ps -axeo "
        for stat in stat_order:
            command += process_info.stat_to_arg[stat] + ","

        return command[:len(command)-1]

    def get_default_stat_order():
        return [process_info.StatType.CPU, process_info.StatType.MEMORY, process_info.StatType.ARGS]

    def __str__(self):
        ret = "Name:" + self.name + "\n"
        ret += "-------------------------\n"
        for (key, value) in self.stat_map.items():
            ret += str(key) + ":" + str(value) + "\n"

        ret = ret[0:-1] + "\n"
        return ret
    def __repr__(self):
        ret = "Name:" + self.name + "= "
        for (key, value) in self.stat_map.items():
            ret += "{" + str(key) + ":" + str(value) + "} "

        ret = ret[0:-1]
        return ret


def run_command(cmd):
    return subprocess.check_output(cmd.split())

def get_cpu_freqs():
    cmd = "grep MHz /proc/cpuinfo"
    return [float(freq) for freq in run_command(cmd).split()[3::4]]

def get_ave_cpu_freq():
    freqs = get_cpu_freqs()
    return sum(freqs)/len(freqs)

def get_normalized_stats():
    stat_order = process_info.get_default_stat_order()
    all_procs = run_command(process_info.get_ps_command_for(stat_order))
    all_procs = [proc.decode("utf-8").split() for proc in all_procs.splitlines()]

    freqs = get_cpu_freqs()
    return [process_info(proc,stat_order,freqs) for proc in all_procs[1:]]

def contains_substring_in(name, strlist):
    for sub in strlist:
        if sub in name:
            return True

    return False

def filter_procs(procs, name_list):
    return [proc for proc in procs if contains_substring_in(proc.get_name(), name_list)]

def record_proc_to_file(output_file, procs):
    for proc in procs:
        to_write = proc.name.rsplit('/',1)[1] + " " + str(proc.get_raw_cpu()) + " " + str(proc.get_stat(process_info.StatType.CPU)) + " " + str(proc.get_stat(process_info.StatType.MEMORY))
        output_file.write(to_write + "\n")

def record_procs(file, filter=None):
    total_mhz_usage = 0.0
    total_mhz = 0.0
    num_samples = 0
    with open(file, 'w+') as proc_file:
        proc_file.write("Time Name CPU Memory\n")
        while not os.path.exists(STOP_RECORDING_FILE):
            procs_to_record = get_normalized_stats()
            if filter:
                procs_to_record = filter_procs(procs_to_record, filter_set)

            total_mhz += get_ave_cpu_freq()
            total_mhz_usage += sum(proc.get_stat(process_info.StatType.CPU) for proc in procs_to_record)
            num_samples = num_samples + 1
            time_to_use = str(time.time())
            proc_file.write(time_to_use + "\n")
            record_proc_to_file(proc_file, procs_to_record)
            time.sleep(0.1)

    print("Average usage from filtered procs MHz " + str(total_mhz_usage/num_samples))
    print("Average cpu MHz " + str(total_mhz/num_samples))
    print("System percent " + str(total_mhz_usage/total_mhz))

def create_proc_data_set(proc_file):
    #not the very effecient, but it works for a first pass
    all_lines = proc_file.read().splitlines()
    header = all_lines[0]
    data = all_lines[1:]

    initial_time = int(float(data[0])*1000)
    curr_time = initial_time

    all_proc_data = [line.split() for line in data if len(line.split()) != 1]
    all_proc_names = {proc_data[0] for proc_data in all_proc_data}

    got_data = set()
    times = [0]
    freq = []
    cpu_for_proc = {name:[] for name in all_proc_names}
    normalized_cpu_for_proc = {name:[] for name in all_proc_names}
    mem_for_proc = {name:[] for name in all_proc_names}

    first_in_time = True
    for data_line in data[1:]:
        split_data = data_line.split()
        if len(split_data) == 1:
            first_in_time = True
            curr_time = int(float(split_data[0])*1000) - initial_time
            times.append(curr_time)
            for proc in all_proc_names:
                if not proc in got_data:
                    cpu_for_proc[proc].append(0)
                    normalized_cpu_for_proc[proc].append(0)
                    mem_for_proc[proc].append(0)

            got_data = set()
        else:
            name = split_data[0]
            cpu_for_proc[name].append(float(split_data[1]))
            normalized_cpu_for_proc[name].append(float(split_data[2])/2000000)
            mem_for_proc[name].append(float(split_data[3]))
            got_data.add(name)

            if first_in_time and cpu_for_proc[name][-1] != 0:
                freq.append(float(split_data[2])/cpu_for_proc[name][-1])
                first_in_time = False

    return (initial_time, freq, times,cpu_for_proc,normalized_cpu_for_proc,mem_for_proc)

def annotate_graph(events, start_time, max_val):
    anno_num = 0
    for event in events:
        split_line = event.split()
        event_time = int(float(split_line[0])*1000) - start_time
        plt.plot([event_time, event_time], [0, max_val], linestyle="-", alpha=0.25)
        name = ' '.join(split_line[1:])

        plt.annotate(name, xy=(event_time, max_val/5*(anno_num+1)))
        anno_num = (anno_num + 1) % 3

def smooth(cpu, patch_size):
    cpucp = cpu.copy();

    for index in range(len(cpucp)):
        total = 0
        num_added = 0
        for inner_index in range(index-patch_size, index+patch_size):
            if inner_index < 0:
                pass
            if inner_index > len(cpu)-1:
                break
            total += cpu[inner_index]
            num_added += 1
        cpucp[index] = total / num_added

    return cpucp


def plot_time_data(times, data, name):
    if name[:2] == "sa":
        plt.plot(times, data, label=name, linestyle="--")
    else:
        plt.plot(times, data, label=name)

def save_plot(events, start_time, max_val, file_name, show_graph=False):
    plt.gcf().set_size_inches(25, 15, forward=True)
    plt.legend(loc='upper right',fancybox=True, framealpha=0.5)
    annotate_graph(events, start_time, max_val)
    plt.savefig(file_name)
    if show_graph:
        plt.show()
    else:
        plt.clf()


def graph_procs(proc_file, event_file, do_show_graph):
    if not event_file == None:
        events = event_file.readlines()
    else:
        events = []

    (start_time, system_frequency, times, cpu_for_proc, norm_cpu_for_proc, mem_for_proc) = create_proc_data_set(proc_file)
    max_val = 0
    plt.xlabel("Time(ms)")
    plt.ylabel("Percent of System Cpu (Unnormalized)")
    for (name, cpu) in cpu_for_proc.items():
        max_val = max(max_val, max(cpu))
        smooth_cpu = smooth(cpu, 10)
        plot_time_data(times, smooth_cpu, name)

    save_plot(events, start_time, max_val, proc_file.name + '_cpu.png', show_graph=do_show_graph)

    plt.xlabel("Time(ms)")
    plt.ylabel("Percent of System Cpu (Normalized to 2GHz)")
    for (name, cpu) in cpu_for_proc.items():
        max_val = max(max_val, max(cpu))
        smooth_cpu = smooth(cpu, 10)
        plot_time_data(times, smooth_cpu, name)

    save_plot(events, start_time, max_val, proc_file.name + '_cpu_normalized.png', show_graph=do_show_graph)

    max_val = 0
    plt.xlabel("Time(ms)")
    plt.ylabel("Percent of System Memory")
    for (name, mem) in mem_for_proc.items():
        max_val = max(max_val, max(mem))
        plot_time_data(times, smooth_cpu, name)
    save_plot(events, start_time, max_val, proc_file.name + '_memory.png', show_graph=do_show_graph)

    plt.xlabel("Time(ms)")
    plt.ylabel("System Frequency (MHz)")
    plot_time_data(times, smooth(system_frequency,5), "Frequency")
    save_plot(events, start_time, max_val, proc_file.name + '_freq.png', show_graph=do_show_graph)

def remove_if_exists(file_name):
    try:
        os.remove(file_name)
    except OSError:
        pass

if __name__ == "__main__":
    action = sys.argv[1]
    if action == "record":
        remove_if_exists(STOP_RECORDING_FILE)
        record_procs(sys.argv[2], sys.argv[3:])
        remove_if_exists(STOP_RECORDING_FILE)
    elif action == "event":
        with open(sys.argv[2], 'a+') as event_file:
            event_file.write(str(time.time()) + " " + ' '.join(sys.argv[3:]) + "\n")
    elif action == "graph":
        with open(sys.argv[2]) as proc_file:
            with open(sys.argv[3]) as event_file:
                show_graph = "show_graph" in ''.join(sys.argv)
                graph_procs(proc_file, event_file,show_graph)
    else:
        print("Commands " + action + " not recognized")
