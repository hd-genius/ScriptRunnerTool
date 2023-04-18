from abc import ABC, abstractmethod
from pathlib import Path
from script import Script


class ScriptHandler(ABC):
    @abstractmethod
    def can_handle(file: Path) -> bool:
        pass

    @abstractmethod
    def create_script_for(file: Path) -> Script:
        pass
