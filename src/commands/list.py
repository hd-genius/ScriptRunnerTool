from .command import register_command
from search import find_all_scripts


@register_command("--list")
def list_scripts():
    print("available scripts:")
    for script in find_all_scripts():
        print(f"  - {script.name}")
