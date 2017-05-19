import os
def remove_if_exists(file_name):
    try:
        os.remove(file_name)
    except OSError:
        pass

def args_to_dir(args):
    good_args = [arg.split('=') for arg in args if "=" in arg]
    bad_args =  [arg for arg in args if not "=" in arg]
    if len(bad_args) > 0:
        print("Ignoring bad arguments: ", bad_args)

    return {key : value for (key, value) in good_args}

def get_existance_lambda(file_name):
    def existance_lambda() : return os.path.exists(file_name)
    return existance_lambda

def array_arg_to_list(arg):
    return arg[1:-1].split(",")