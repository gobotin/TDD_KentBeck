"""テストコード"""
# pyrefly: ignore [missing-import]
from money import Money
# pyrefly: ignore [missing-import]
from bank import Bank
# pyrefly: ignore [missing-import]
from sum import Sum
# pyrefly: ignore [missing-import]
from expression import Expression

class TestMoney():
    """Moneyクラスのテスト"""
    def test_multiplication(self):
        """金額を指定倍する"""
        five: Money = Money.dollar(5)
        assert Money.dollar(10) == five.times(2), "5 * 2"
        assert Money.dollar(15) == five.times(3), "5 * 3"

    def test_equality(self):
        """同一性テスト"""
        assert Money.dollar(5) == Money.dollar(5), "$5 == $5"
        assert not (Money.dollar(5) == Money.dollar(6)), "$5 != $6"
        assert not (Money.franc(5) == Money.dollar(5)), "f5 != $5"

    def test_currency(self):
        """通貨単位のテスト"""
        assert "USD" == Money.dollar(1).getval_currency(), "Dollar Unit"
        assert "CHF" == Money.franc(1).getval_currency(), "Franc Unit"

    def test_simple_addition(self):
        """
        同一単位の加算
            数値と単位が等しいかのテスト
            確認したいのはbank経由でSum.reduceの加算がちゃんとできているか
            plusメソッドのテストも兼ねている
        """
        five = Money.dollar(5)
        # sum = 5$ + 5$
        sum: Sum = five.plus(five) # Money.dollar(5).plus(Money.dollar(5))
        bank = Bank()
        reduced = bank.reduce(sum, "USD")
        assert Money.dollar(10) == reduced, "equal"

    def test_plus_returnsum(self):
        """
        加算結果がSumオブジェクトで返されるかのテスト
        """
        five = Money.dollar(5)
        result: Sum = five.plus(five)
        assert five == result.getobj_augend()
        assert five == result.getobj_addend()

    def test_reduce_sum(self):
        """
        Sum.reduceのテスト
            Sumオブジェクトの加算結果がMoneyオブジェクトで返されるかのテスト
        sinmple_additionとの違い
            plusメソッドを使用せずにBank → Sum → Money.reduceの順で実行
        """
        # sum = 3$ + 4$
        sum = Sum(Money.dollar(3), Money.dollar(4))
        bank = Bank()
        result = bank.reduce(sum, "USD")
        assert Money.dollar(7) == result

    def test_reduce_money(self):
        """
        両替の下準備
            同じ通貨であれば、そのまま返ってくることを確認
        """
        bank = Bank()
        result = bank.reduce(Money.dollar(1), "USD")
        assert Money.dollar(1) == result, "Money as expression"

    def test_reduce_money_different_currency(self) -> None:
        """
        異なる通貨での為替レート計算のテスト
        """
        bank = Bank()
        bank.addRate("CHF", "USD", 2) # 1ドル = 2フラン
        result = bank.reduce(Money.franc(2), "USD")
        assert Money.dollar(1) == result

    def test_identy_rate(self) -> None:
        """
        同一通貨の為替レートが1であることを確認
        """
        assert 1 == Bank().rate("USD", "USD")

    def test_mixed_addiction(self) -> None:
        """
        異なる通貨の混合加算
        """
        fiveBucks: Money = Money.dollar(5)
        tenFrancs: Expression = Money.franc(10)
        bank = Bank()
        bank.addRate("CHF", "USD", 2) # 1ドル = 2フラン
        result: Money = bank.reduce(fiveBucks.plus(tenFrancs), "USD")
        assert Money.dollar(10) == result
