#!/usr/bin/env python
import argparse        # To parse command line arguments

ARGS = None

PIPELINE_STEPS = []
step = lambda f: PIPELINE_STEPS.append((f.__name__, f))

def main():
    global ARGS
    ARGS = parse_command_line_arguments()
    execute()

def parse_command_line_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', type=str, dest='step',
        choices=['checkout', 'reset'], required=False, action='store', help="Pipeline step to execute")
    return parser.parse_args()

def execute():
    if ARGS is not None:
        if ARGS.step is not None:
            if ARGS.step == "reset":
                reset_repository()
            elif ARGS.step == "exists":
                check_revision_exists()
            elif ARGS.step == "checkout":
                checkout_revision()
            elif ARGS.step == "":
                reset_repository()
        else:  # Execute whole pipeline
            for step_name, execute_step in PIPELINE_STEPS:
                print step_name
                execute_step()
    else:
        print "ARGS is None"

@step
def check_revision_exists():
    pass

@step
def checkout_revision():
    pass

@step
def reset_repository():
    pass

if __name__ == "__main__":
    main()

