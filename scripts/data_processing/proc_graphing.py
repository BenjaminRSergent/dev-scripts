import numpy as np
import matplotlib.pyplot as plt

def smooth(data_set, patch_size):
    datacp = data_set.copy();

    for index in range(len(datacp)):
        total = 0
        num_added = 0
        for inner_index in range(index-patch_size, index+patch_size):
            if inner_index < 0:
                pass
            if inner_index > len(data_set)-1:
                break
            total += data_set[inner_index]
            num_added += 1
        datacp[index] = total / num_added

    return datacp

class process_data_set:
    def __init__(self, name, times):
        self.name = name
        self.times = times
        self.cpu_percent = np.zeros(times.shape)
        self.cpu_mhz = np.zeros(times.shape)
        self.memory = np.zeros(times.shape)

    def set_at_index(self, index, cpu_percent, cpu_mhz, memory):
        self.cpu_percent[index] = cpu_percent
        self.cpu_mhz[index] = cpu_mhz
        self.memory[index] = memory

class process_graph:
    def __init__(self, data_file_name, event_file_name=None, proc_filter=None):
        self.data_file_name = data_file_name
        self.event_file_name = event_file_name
        self.proc_filter = proc_filter

    def create_graphs(self, save=True, show=True):
        self.create_data_set()

        if self.event_file_name:
            self.events = self.load_file(self.event_file_name)
        else:
            self.events = []

        self.plot_data(save, show)

    def annotate_graph(self, max_val):
        anno_num = 0

        for event in self.events:
            event_time = self.normalize_time(float(event[0]))
            event_name = ' '.join(event[1:])
            plt.plot([event_time, event_time], [0, max_val], linestyle="-")
            print(event_time)
            #plt.annotate(event_name, xy=(event_time, max_val/5*(anno_num+1)))
            anno_num = (anno_num + 1) % 3

    def create_data_set(self):
        data = np.array(self.load_file(self.data_file_name)[1:])
        self.times = np.array([float(time_val) for time_val in np.unique(data[:,0])])

        self.start_time = float(self.times[0])
        self.times = self.normalize_time(self.times)
        self.proc_names = np.unique(data[:,1])
        self.proc_data_dir = {name : process_data_set(name, self.times) for name in self.proc_names}

        data_lines = data[:,1:]
        index = 0
        for data_time in self.times:
            all_data_at_time = data[data[:,0] == str(data_time)]
            for data_at_time in all_data_at_time:
                self.proc_data_dir[data_at_time[1]].set_at_index(index, data_at_time[2], data_at_time[3], data_at_time[4])
            index = index+1


    def plot_data(self, save, show):
        max_val = 0
        plt.xlabel("Time(ms)")
        plt.ylabel("Percent of System Cpu (Unnormalized)")
        for (name, proc_data) in self.proc_data_dir.items():
            max_val = max(max_val, max(proc_data.cpu_percent))
            self.plot_time_data(smooth(proc_data.cpu_percent, 15), name)

        self.setup_graph(max_val)
        if save:
            self.finish_current_plot(show, file_name=(self.data_file_name + "_cpu_percent_unnormalized.png"))
        else:
            self.finish_current_plot(show)

        plt.xlabel("Time(ms)")
        plt.ylabel("Percent of System Cpu (Normalized to 2.4GHz)")
        norm_value = 2400000
        max_val = 0
        for (name, proc_data) in self.proc_data_dir.items():
            norm_cpu = proc_data.cpu_mhz/norm_value*100
            max_val = max(max_val, max(norm_cpu))
            self.plot_time_data(smooth(norm_cpu,15), name)

        self.setup_graph(max_val)
        if save:
            self.finish_current_plot(show, file_name=(self.data_file_name + "_cpu_normalized.png"))
        else:
            self.finish_current_plot(show)

        max_val = 0
        plt.xlabel("Time(ms)")
        plt.ylabel("Percent of System Memory")
        for (name, proc_data) in self.proc_data_dir.items():
            max_val = max(max_val, max(proc_data.memory))
            self.plot_time_data(proc_data.memory, name)

        self.setup_graph(max_val)
        if save:
            self.finish_current_plot(show, file_name=(self.data_file_name + "_memory.png"))
        else:
            self.finish_current_plot(show)

    def plot_time_data(self, data, name):
        if name[:2] == "sa":
            plt.plot(self.times, data, label=name, linestyle="--")
        else:
            plt.plot(self.times, data, label=name)

    def setup_graph(self, max_val):
        self.annotate_graph(max_val)
        plt.legend(loc='upper right',fancybox=True, framealpha=0.5)

    def finish_current_plot(self, show, file_name=None):
        plt.gcf().set_size_inches(25, 15, forward=True)

        if file_name:
            plt.savefig(file_name)
        if show:
            plt.show()
        plt.clf()

    def load_file(self,file_name):
        with open(file_name) as file:
            return [line.split() for line in file.readlines()]

    def normalize_time(self, time_to_norm):
        return (time_to_norm - self.start_time)*1000