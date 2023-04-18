from pathlib import Path
from api import register_handler, ScriptHandler, Script


@register_handler
class PowershellHandler(ScriptHandler):
    def can_handle(file: Path) -> bool:
        return file.suffix is ".ps1"

    def create_script_for(file: Path) -> Script:
        return PowerShellScript(file)


class PowerShellScript(Script):
    name = ""
    path = ""
    def __init__(self, file: Path) -> None:
        super().__init__()
        self.name = file.name
        self.path = file

    def execute():
        pass
