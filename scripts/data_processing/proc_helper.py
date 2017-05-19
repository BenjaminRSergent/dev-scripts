import proc_recording
import proc_graphing
import time
import sys
from main_utils import *

STOP_RECORDING_FILE = "./.stop_recording"

def print_usage():
    print("Usage:")
    print("------")
    print("Recording. The filter is optional")
    print("python3 proc_helper.py record data_file=file_name filter=[proc_name1, proc_name2,...]")
    print()
    print("The recording will continue until the following is called from a different terminal:")
    print("python3 proc_helper.py stop_recording")
    print("------")
    print("Adding events for graph annotation. This is done while the recording is taking place to match the data timestamps.")
    print("python3 proc_helper.py event_file=event_file event_name=\"Event name\"")
    print()
    print("The event will be appended to the event file with a timestamp.")
    print("The event file can be used by the graph command to add annotations")
    print("------")
    print("Graphing. The event file and filter are optional")
    print("python3 proc_helper.py graph data_file=file_name event_file=file_name filter=[proc_name1, proc_name2,...]")

def start_recording(args):
    if not "data_file" in args:
        print("No data file for recording!\n")
        print_usage()
        return

    remove_if_exists(STOP_RECORDING_FILE)
    if "filter" in args:
        proc_recording.record_procs(args["data_file"], get_existance_lambda(STOP_RECORDING_FILE), filter=array_arg_to_list(args["filter"]))
    else:
        proc_recording.record_procs(args["data_file"], get_existance_lambda(STOP_RECORDING_FILE))
    remove_if_exists(STOP_RECORDING_FILE)

def stop_recording():
    open(STOP_RECORDING_FILE, 'w+')

def record_event(args):
    if not "event_file" in args or not "event_name" in args:
        print("Missing arguments for event recording!\n")
        print_usage()
        return

    with open(args["event_file"], 'a+') as event_file:
        event_file.write(str(time.time()) + " " + args["event_name"] + "\n")

def make_graph(args):
    if not "data_file" in args:
        print("No data file for graph!\n")
        print_usage()
        return

    data_file = args["data_file"]
    event_file = None if not "event_file" in args else args["event_file"]
    proc_filter = None if not "filter" in args else args["filter"]

    graph = proc_graphing.process_graph(data_file, event_file_name=event_file, proc_filter=proc_filter)
    graph.create_graphs()

if __name__ == "__main__":
    action = sys.argv[1]
    args = args_to_dir(sys.argv[2:])
    if "help" in action or action == "-h":
        print_usage()
    elif action == "record":
        start_recording(args)
    elif action == "stop_recording":
        stop_recording()
    elif action == "event":
        record_event(args)
    elif action == "graph":
        make_graph(args)
    else:
        print("Commands " + action + " not recognized")
        print_usage()
