#!/usr/bin/env -S python3 -B

import os
from subprocess import check_output


if __name__ == "__main__":
    print("Hello world!")
    print(os.getcwd())
    print(check_output(['ls','-larth']))

    with open('gource-log.log','r') as f:
        print(f.read())