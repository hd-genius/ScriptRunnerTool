#!/usr/bin/env python3

import sys
from runr.plugins import load_plugins
from runr.commands import is_program_command, run_command
from runr.search import find_script_with_name
from runr.errors import ApplicationError


def main():
    try:
        load_plugins()
        first_argument = sys.argv[1]
        if (is_program_command(first_argument)):
            run_command(first_argument)
        else:
            run_script(first_argument)
    except ApplicationError as error:
        error.print()


def run_script(script_name):
    script_to_run = find_script_with_name(script_name)
    script_to_run.execute()


if __name__ == "__main__":
    main()
