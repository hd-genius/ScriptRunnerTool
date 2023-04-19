from abc import ABC, abstractmethod
from pathlib import Path

class Script(ABC):
    name: str
    path: Path
    
    def __init__(self, file: Path) -> None:
        super().__init__()
        self.name = file.stem
        self.path = file

    @abstractmethod
    def execute():
        pass
