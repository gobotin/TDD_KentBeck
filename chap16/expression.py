from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING 

if TYPE_CHECKING:
    # pyrefly: ignore [missing-import]
    from money import Money
    # pyrefly: ignore [missing-import]
    from bank import Bank


class Expression(metaclass=ABCMeta):
    @abstractmethod
    def reduce(self, bank: Bank, to: str) -> Money:  # pragma: no cover
        pass

    @abstractmethod
    def plus(self, addend: Expression) -> Expression:  # pragma: no cover
        pass

    @abstractmethod
    def times(self, multiplier: int) -> Expression:  # pragma: no cover
        pass