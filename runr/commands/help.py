from .command import register_command


@register_command("--help")
def print_help():
    print("help text")
