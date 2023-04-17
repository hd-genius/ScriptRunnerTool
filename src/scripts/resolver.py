import os
from pathlib import Path
from collections import namedtuple


ScriptLocator = namedtuple('ScriptLocator', 'name path')

def find_script_with_name(name: str) -> callable:
    files_with_name = list(filter(lambda x: x.name == name, _find_scripts()))
    _verify_matching_scripts(name, files_with_name)
    return files_with_name[0].path

def _verify_matching_scripts(script_name, scripts):
    scripts_count = len(scripts)
    if (scripts_count == 0):
        raise InvalidScriptNameError(script_name)
    elif (scripts_count > 1):
        raise ConflictingScriptNamesError(script_name, scripts)

def _find_scripts():
    scripts_location = os.environ['SCRIPTER_SCRIPTS']
    script_paths = list(filter(_is_script, _all_files_under_folder(scripts_location)))
    return map(_script_locator_for_path, script_paths)

def _script_locator_for_path(path):
    return ScriptLocator(path.stem, path)

def _all_files_under_folder(folderPath: str):
    return [ Path(os.path.join(root, fileName)) for root, directories, files in os.walk(folderPath) for fileName in files ]

def _is_script(path: Path):
    return path.suffix in ['.ps1', '.py', '.js', '.sh']

class InvalidScriptNameError(Exception):
    def __init__(self, filename):
        super()
        self.filename = filename

class ConflictingScriptNamesError(Exception):
    def __init__(self, filename, conflicting_paths):
        super()
        self.filename = filename
        self.conflicting_paths = conflicting_paths