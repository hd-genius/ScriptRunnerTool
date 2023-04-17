#!/usr/bin/env python3

import sys
from plugins import load_plugins
from commands import is_program_command, run_command

def main():
    first_argument = sys.argv[1]
    if (is_program_command(first_argument)):
        run_command(first_argument)
    else:
        run_script()

def run_script():
    load_plugins()
    # find script
    # run script
    print("Hello World!")

if __name__ == "__main__":
    main()
