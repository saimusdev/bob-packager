#!/usr/bin/env python
import argparse        # To parse command line arguments

ARGS = None

def main():
    print "Hello World!"
    ARGS = parse_command_line_arguments()
    execute()

def parse_command_line_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--step", required=False, action="store_true", help="Pipeline step to execute")
    return parser.parse_args()

def execute():
    if ARGS is not None:
        if ARGS.step == "checkout":
            checkout_revision()
        elif ARGS.step == "reset":
            reset_repository()

def checkout_revision():
    print "CHECKOUT"

def reset_repository():
    print "RESET"

if __name__ == "__main__":
    main()

