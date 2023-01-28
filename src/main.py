import sys
from src.plugins import load_plugins

def main():
    first_argument = sys.argv[1]
    if (is_program_command(first_argument)):
        run_command(first_argument)
    else:
        run_script()

def is_program_command(value) -> bool:
    pass

def run_command(command):
    match(command):
        case "--list":
            print("available scripts")
        case "--help":
            print("help text")
        case _:
            raise UnrecognizedCommandError(command)

def run_script():
    load_plugins()
    # find script
    # run script
    print("Hello World!")

class UnrecognizedCommandError(Exception):
    def __init__(self, command):
        super()
        self.command = command

if __name__ == "__main__":
    main()
