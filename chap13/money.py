"""通貨クラス"""
from __future__ import annotations
# pyrefly: ignore [missing-import]
from expression import Expression

class Money(Expression):
    """通貨"""

    def __init__(self, amount: int, currency: str) -> None:
        """初期化"""
        self._amount = amount
        self._currency = currency

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):  # pragma: no cover
            return False
        return (self._amount == other._amount) and (self._currency == other._currency)

    def times(self, multiplier: int) -> Money:
        """金額を指定倍して返す"""
        return Money(self._amount * multiplier, self._currency)

    def plus(self, addend: Money) -> Expression:
        """加算"""
        # pyrefly: ignore [missing-import]
        from sum import Sum
        return Sum(self, addend)

    def reduce(self, to: str) -> Money:
        return self

    def getval_amount(self) -> int:
        """amountに直接アクセスしないためのメソッド"""
        return self._amount

    def getval_currency(self) -> str:
        """currencyに直接アクセスしないためのメソッド"""
        return self._currency

    @staticmethod
    def dollar(amount: int) -> Money:
        """ドルを作成して、返す"""
        return Money(amount, "USD")

    @staticmethod
    def franc(amount: int) -> Money:
        """フランを作成して、返す"""
        return Money(amount, "CHF")