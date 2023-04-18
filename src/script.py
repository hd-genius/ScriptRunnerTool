from abc import ABC, abstractmethod

class Script(ABC):
    name = ""
    path = ""

    @abstractmethod
    def execute():
        pass
