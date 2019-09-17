#!/usr/bin/env python
import argparse        # To parse command line arguments

ARGS = None

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
        if ARGS.step == "checkout":
            checkout_revision()
        elif ARGS.step == "reset":
            reset_repository()
    else:
        print "ARGS is None"

def checkout_revision():
    print "CHECKOUT"

def reset_repository():
    print "RESET"

if __name__ == "__main__":
    main()

