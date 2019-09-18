#!/usr/bin/env python
import os              # To access filesystem
import argparse        # To parse command line arguments
import git             # For working with Git repos
import json            # To parse JSON config file

ARGS = None
CONFIG_FILEPATH = 'example-config.json'
CONFIG = None

PIPELINE_STAGES = []
# Function decorator to append step to pipeline
def stage(s):
    PIPELINE_STAGES.append((s.__name__, s)) # Executed at start time
    def stage_wrapper(): # Executed at runtime
        print s.__name__
        s()
    return stage_wrapper

def main():
    global ARGS, CONFIG
    ARGS = parse_command_line_arguments()
    CONFIG = parse_configuration_file()
    if ARGS is not None and CONFIG is not None:
        execute()

def parse_command_line_arguments():
    parser = argparse.ArgumentParser()
    possible_stages,_ = map(list,zip(*PIPELINE_STAGES))
    parser.add_argument(
        'CONFIG', 
        type=str,
        action='store',
        help="Configuration file")
    parser.add_argument(
        '-s', 
        type=str,
        dest='stage',
        choices=possible_stages,
        required=False,
        action='store',
        help="Pipeline stage to execute")
    return parser.parse_args()

def parse_configuration_file():
    global CONFIG
    with open(CONFIG_FILEPATH) as f:
        return json.load(f)

def execute():
    if ARGS.stage is not None:
        globals()[ARGS.stage]() # Call function with the same name
    else:  # Execute whole pipeline
        for stage_name, execute_stage in PIPELINE_STAGES:
            print "--> stage: %s" % stage_name
            execute_stage()

@stage
def clone():
    remote_url = CONFIG['repo']['remote']
    local_repo = CONFIG['repo']['name'] 
    if not os.path.exists(local_repo):
            repo = git.Repo.clone_from(
                remote_url, 
                local_repo,
                branch='master',
                progress=git.remote.RemoteProgress())
    else:
        try:
            _ = git.Repo(local_repo).git_dir
            print "repo already cloned, skipping..."
        except git.exc.InvalidGitRepositoryError:
            print "Error: directory already exists with same name as repo"

@stage
def reset():
    try:
        repo = git.Repo(CONFIG['repo']['name'])
    except git.exc.NoSuchPathError:
        print "Cannot reset inexistent repo" 

@stage
def exists():
    pass

@stage
def checkout():
    pass

@stage
def prepare():
    pass

@stage
def clean():
    pass

@stage
def build():
    pass

@stage
def package():
    pass

if __name__ == "__main__":
    main()

