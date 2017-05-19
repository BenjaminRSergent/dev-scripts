import sys
import os
import subprocess
from enum import Enum


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
        command = "ps -aeo "
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