#!/usr/bin/env -S python3 -B

import os
from subprocess import check_output, CalledProcessError

def add_checkout_as_safe_directory():
    try:
        check_output(['git','config','--global','--add','safe.directory','/github/workspace'])
    except CalledProcessError:
        print("Warning: Could not configure github workspace as a safe directory!")


def run_gource_and_store_log(log_file_name):
    check_output(['gource','--output-custom-log',log_file_name])

if __name__ == "__main__":
    print("Hello world!")
    print(os.getcwd())
    fname = 'gource-log.log'

    add_checkout_as_safe_directory()
    run_gource_and_store_log(fname)

    with open(fname,'r') as f:
        print(f.read())