commands = {}


def register_command(name: str):
    def add_command(command: callable):
        commands[name] = command
        return command
    return add_command


def is_program_command(value: str) -> bool:
    pass


def run_command(command: str):
    if command in commands:
        command_to_execute = commands[command]
        command_to_execute()
    else:
        raise UnrecognizedCommandError(command)


class UnrecognizedCommandError(Exception):
    def __init__(self, command):
        super()
        self.command = command
