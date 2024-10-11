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


def highlight_log_by_names(log_file,names):

    colors = ["#474747","#E4E4E4"]


    with open(log_file, 'r') as f:
        log_lines = f.readlines()


    with open(log_file,'w') as f:
        for line in log_lines:
            fields = line.split('|')

            color = colors[0]
            #print(fields[1])
            for name in names:
                if name in fields[1]:
                    color = colors[1]
                    break
                    
            
            new_line = line.strip() + f"|{color}"
            
            #print(new_line)
            f.write(new_line + '\n')



def colorize_log_by_project(log_file):

    colors = [
        # Define a set of colors
        "#3357FF","#33FF57","#FAAAAA",
        "#FF33A1","#33FFF5", "#FFD733","#A133FF","#FF8C33","#DDFFDA","#3333AF"
    ]

    associations = {}

    with open(log_file, 'r') as f:
        log_lines = f.readlines()

    current_color = 0
    with open(log_file,'w') as f:
        for line in log_lines:
            fields = line.split('|')
            path_parts = fields[3].split('/')

            base_dir = path_parts[1]
            #print(base_dir)
            if not associations.get(base_dir):
                associations[base_dir] = colors[current_color % len(colors)]
                current_color += 1
            
            color = associations[base_dir]
            new_line = line.strip() + f"|{color}"
            #print(new_line)
            f.write(new_line + "\n")



if __name__ == "__main__":
    print("Hello world!")
    print(os.getcwd())
    fname = 'gource-log.log'

    add_checkout_as_safe_directory()
    run_gource_and_store_log(fname)

    with open(fname,'r') as f:
        print(f.read())