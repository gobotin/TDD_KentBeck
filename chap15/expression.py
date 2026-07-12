from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING 

if TYPE_CHECKING:
    # pyrefly: ignore [missing-import]
    from money import Money
    # pyrefly: ignore [missing-import]
    from bank import Bank


class Expression(metaclass=ABCMeta):
    """式（演算）を表します。"""

    @abstractmethod
    def reduce(self, bank: Bank, to: str) -> Money:  # pragma: no cover
        """式を単純な形に変形する"""
        pass