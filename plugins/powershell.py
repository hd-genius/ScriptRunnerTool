from pathlib import Path
import subprocess
from api import register_handler, ScriptHandler, Script

@register_handler
class PowershellHandler(ScriptHandler):
    def can_handle(self, file: Path) -> bool:
        return file.suffix == ".ps1"

    def create_script_for(self, file: Path) -> Script:
        return PowerShellScript(file)


class PowerShellScript(Script):
    def __init__(self, file: Path) -> None:
        super().__init__(file)

    def execute(self):
        subprocess.run(f"PowerShell -File {self.path}")
