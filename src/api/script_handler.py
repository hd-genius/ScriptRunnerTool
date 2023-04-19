from abc import ABC, abstractmethod
from pathlib import Path
from .script import Script


class ScriptHandler(ABC):
    """The abstract base class for script handler plugins."""
    @abstractmethod
    def can_handle(file: Path) -> bool:
        """A method that determines if the ScriptHandler can handle a file"""
        pass

    @abstractmethod
    def create_script_for(file: Path) -> Script:
        """Creates a Script object representation of the given file"""
        pass
