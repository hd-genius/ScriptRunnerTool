from abc import ABC, abstractmethod
from pathlib import Path


class Script(ABC):
    """The base class representing a script that can be executed"""
    name: str
    path: Path

    def __init__(self, file: Path) -> None:
        self.name = file.stem
        self.path = file

    @abstractmethod
    def execute(self):
        """Runs the script file that this object represents"""
        pass
