import os
from pathlib import Path
from importlib import import_module

plugin_module_directory = Path(__file__).parent.resolve()


def load_plugins():
    for plugin in _find_all_plugins():
        _load_plugin(plugin)


def _load_plugin(plugin: Path):
    import_module("plugins." + plugin.stem)


def _find_all_plugins():
    file_names = os.listdir(plugin_module_directory)
    files = [_path_for_plugin(x) for x in file_names]
    return [x for x in files if _is_plugin(x)]


def _is_plugin(file: Path):
    plugin_source_files = ["__init__.py", "load.py"]
    return file.suffix == ".py" and file.name not in plugin_source_files


def _path_for_plugin(name):
    return Path(os.path.join(plugin_module_directory, name))
