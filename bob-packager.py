#!/usr/bin/env python
import argparse        # To parse command line arguments

ARGS = None

PIPELINE_STEPS = []
# Function decorator to append step to pipeline
def step(s):
    PIPELINE_STEPS.append((s.__name__, s)) # Executed at start time
    def step_wrapper(): # Executed at runtime
        print s.__name__
        s()
    return step_wrapper

def main():
    global ARGS
    ARGS = parse_command_line_arguments()
    execute()

def parse_command_line_arguments():
    parser = argparse.ArgumentParser()
    possible_steps,_ = map(list,zip(*PIPELINE_STEPS))
    parser.add_argument(
        '-s', 
        type=str,
        dest='step',
        choices=possible_steps,
        required=False,
        action='store',
        help="Pipeline step to execute")
    return parser.parse_args()

def execute():
    if ARGS is not None:
        if ARGS.step:
            if ARGS.step == "reset":
                reset()
            elif ARGS.step == "exists":
                exists()
            elif ARGS.step == "checkout":
                checkout()
            elif ARGS.step == "prepare":
                prepare()
            elif ARGS.step == "clean":
                clean()
            elif ARGS.step == "build":
                build()
            elif ARGS.step == "package":
                package()
        else:  # Execute whole pipeline
            for step_name, execute_step in PIPELINE_STEPS:
                print step_name
                execute_step()
    else:
        print "ARGS is None"

@step
def reset():
    pass

@step
def exists():
    pass

@step
def checkout():
    pass

@step
def prepare():
    pass

@step
def clean():
    pass

@step
def make():
    pass

@step
def package():
    pass

if __name__ == "__main__":
    main()

