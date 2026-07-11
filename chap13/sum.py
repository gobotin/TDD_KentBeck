"""金額合計"""
# pyrefly: ignore [missing-import]
from expression import Expression
# pyrefly: ignore [missing-import]
from money import Money

class Sum(Expression):
    """金額の合計を表します。"""

    def __init__(self, augend: Money, addend: Money) -> None:
        """初期化"""
        self._augend = augend
        self._addend = addend

    def getobj_augend(self):
        return self._augend

    def getobj_addend(self):
        return self._addend

    def reduce(self, to: str) -> Money:
        """式を単純な形に変形する"""
        # augendとaddedは両方オブジェクト
        self._amount = self.getobj_augend().getval_amount() + self.getobj_addend().getval_amount()
        return Money(self._amount, to)

        """
        test_sinple_additionの場合
            self: Sum(中身はMoney)
                Sum型は、_augendと_addendのオブジェクトを持つ
                今回は両方Money.dollar(5)が入っている。(アドレスは違う)
            加算結果をMoney型に渡している
        """
            
        