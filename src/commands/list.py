from .command import register_command

@register_command("--list")
def list_scripts():
    print("available scripts")