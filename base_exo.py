from abc import ABC, abstractmethod
from wrapper import Wrapper
from typing import Tuple, Callable

class BaseExo(ABC):
    name: str

    @abstractmethod
    def execute(self) -> Wrapper:
        pass

class BaseTP():
    name: str
    tp_exo_list: Tuple[Callable[[], Wrapper]]