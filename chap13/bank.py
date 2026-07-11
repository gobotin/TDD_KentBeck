"""銀行"""
# pyrefly: ignore [missing-import]
from expression import Expression
# pyrefly: ignore [missing-import]
from money import Money

class Bank:
    """銀行を表します。"""
    def reduce(self, source: Expression, to: str) -> Money:
        """いずれ為替レートの計算をするメソッド"""
        return source.reduce(to)

        """
        test_sinple_additionの場合
            source: Sumなので、source.reduceはSumクラスの
            reduceメソッドが実行される
            Sum.reduceの戻り値がMoneyなので、このメソッドもMoneyが返される
        """