from proc_utils import *
import time

def record_proc_to_file(output_file, time_stamp, procs):
    for proc in procs:
        proc_name = proc.name.rsplit('/',1)[1] if '/' in proc.name else proc.name
        to_write = str(time_stamp) + " " + proc_name + " " + str(proc.get_raw_cpu()) + " " + str(proc.get_stat(process_info.StatType.CPU)) + " " + str(proc.get_stat(process_info.StatType.MEMORY))
        output_file.write(to_write + "\n")

def record_procs(file_name, stop_condition, filter=None, sec_between_samples=0.1):
    total_percent_usage = 0.0
    total_system_percent = 0.0
    total_ave_mhz = 0.0
    total_max_mhz = 0.0
    num_samples = 0
    start = time.time()

    if filter:
        print("Writing process data filtered by " + str(filter) + " to " + file_name)
    else:
        print("Writing all processes filtered to " + file_name)

    with open(file_name, 'w+') as proc_file:
        proc_file.write("Time Name CPU Memory\n")
        while not stop_condition():
            procs_to_record = get_normalized_stats()
            total_system_percent += sum(proc.get_raw_cpu() for proc in procs_to_record)
            if filter:
                procs_to_record = filter_procs(procs_to_record, filter)
                total_percent_usage += sum(proc.get_raw_cpu() for proc in procs_to_record)
            else:
                total_percent_usage = total_system_percent

            total_ave_mhz += get_ave_cpu_freq()
            total_max_mhz += max(get_cpu_freqs())

            num_samples = num_samples + 1
            record_proc_to_file(proc_file, time.time(), procs_to_record)
            time.sleep(sec_between_samples)

    end = time.time()
    format_to_use = "{0:.2f}"

    print("Finished writing to " + file_name)
    print("Length of recording: " + format_to_use.format(end - start) + " seconds")
    print("Estimated average percent of total system cpu used from recorded procs: " + format_to_use.format(total_percent_usage/num_samples) + "%")
    print("Estimated average percent of system activity from recorded procs: " + format_to_use.format(total_percent_usage/total_system_percent * 100) + "%")

    print("Average peak cpu MHz (average of max between cores): " + format_to_use.format(total_max_mhz/num_samples))
    print("Average cpu MHz between all cores: " + format_to_use.format(total_ave_mhz/num_samples))