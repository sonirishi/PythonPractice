from typing import runtime_checkable, Protocol
from abc import abstractmethod

@runtime_checkable
class support_complex(Protocol):

    @abstractmethod
    def __complex__(self) -> complex:
        pass

