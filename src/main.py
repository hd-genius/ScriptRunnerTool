#!/usr/bin/env python3

import sys
from plugins import load_plugins
from commands import is_program_command, run_command
from scripts import find_script_with_name


def main():
    first_argument = sys.argv[1]
    if (is_program_command(first_argument)):
        run_command(first_argument)
    else:
        run_script(first_argument)


def run_script(script_name):
    load_plugins()
    script_to_run = find_script_with_name(script_name)
    script_to_run()


if __name__ == "__main__":
    main()
