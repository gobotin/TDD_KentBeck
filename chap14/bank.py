from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # pyrefly: ignore [missing-import]
    from expression import Expression
    # pyrefly: ignore [missing-import]
    from money import Money

# pyrefly: ignore [missing-import]
from pair import Pair


class Bank:
    """為替レートの計算をする、銀行クラス"""
    def __init__(self) -> None:
        self._rates: dict[Pair, int] = {}

    def reduce(self, source: Expression, to: str) -> Money:
        """いずれ為替レートの計算をするメソッド"""
        return source.reduce(self, to)
        """
        test_sinple_additionの場合
            source: Sumなので、source.reduceはSumクラスの
            reduceメソッドが実行される
            Sum.reduceの戻り値がMoneyなので、このメソッドもMoneyが返される
        
        test_reduce_money_different_currencyの場合
            source: 2CHFのMoneyクラス
            to: "USD"
            bank.rate("CHF", "USD")が1/2を返す
            
        """

    def addRate(self, from_: str, to: str, rate: int) -> None:
        """貨幣レートの変換を辞書に登録"""
        # 辞書に登録
        self._rates[Pair(from_, to)] = rate

    def rate(self, from_: str, to: str) -> int:
        """為替レートの値を取得"""
        if (from_ == to):
            return 1
        # getメソッドは、pythonの辞書の標準メソッド: 
        #   引数でkeyを渡し、valueを取得する
        rate = self._rates.get(Pair(from_, to))
        
        # 辞書に登録されていない場合はNoneが返されるので、例外処理
        if (rate is None):  # pragma: no cover
            raise ValueError(f"{from_} to {to}のレートが設定されていません")
        return rate
        """
        test_reduce_money_diffent_currencyの場合
            self: Bank
            from_: "CHF"
            to: "USD"
        """
