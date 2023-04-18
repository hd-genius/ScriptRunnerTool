import os
from pathlib import Path
from collections import namedtuple
from errors import InvalidScriptNameError, ConflictingScriptNamesError, ConfigurationError
from script import Script
from api import script_handlers


ScriptLocator = namedtuple('ScriptLocator', 'name path')

SCRIPTS_HOME_VARIABLE = "SCRIPT_RUNNER_DIR"


def find_script_with_name(name: str) -> Script:
    scripts_with_name = [x for x in find_all_scripts() if x.name is name]
    _verify_matching_scripts(name, scripts_with_name)
    return scripts_with_name[0]


def find_all_scripts() -> list[Script]:
    if SCRIPTS_HOME_VARIABLE not in os.environ:
        raise ConfigurationError(
            'The environment variable "SCRIPT_RUNNER_DIR" is not set.')
    scripts_location = os.environ[SCRIPTS_HOME_VARIABLE]
    script_paths = [x for x in _all_files_under_folder(
        scripts_location) if _is_script(x)]
    return [script for path in script_paths for script in _all_scripts_for_file(path)]


def _verify_matching_scripts(script_name, scripts):
    scripts_count = len(scripts)
    if (scripts_count == 0):
        raise InvalidScriptNameError(script_name)
    elif (scripts_count > 1):
        raise ConflictingScriptNamesError(script_name, scripts)


def _all_files_under_folder(folderPath: str):
    return [Path(os.path.join(root, fileName)) for root, directories, files in os.walk(folderPath) for fileName in files]


def _all_scripts_for_file(file: Path) -> list[Script]:
    capable_handlers = [x for x in script_handlers if x.can_handle(file)]
    return [x.create_script_for(file) for x in capable_handlers]


def _is_script(path: Path):
    script_compatabilities = [x.can_handle(path) for x in script_handlers]
    return any(script_compatabilities)
