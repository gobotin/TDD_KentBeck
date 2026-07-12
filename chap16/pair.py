"""通貨間の為替レートを管理するクラス"""

class Pair:
    """変換元と変換先の通貨のペアを表します。"""

    def __init__(self, from_: str, to: str) -> None:
        """初期化"""
        self._from = from_
        self._to = to

    def __eq__(self, other: object) -> bool:
        """同一性の検証"""
        if not isinstance(other, Pair):  # pragma: no cover
            return NotImplemented
        return (self._from == other._from) and (self._to == other._to)

    def __hash__(self) -> int:
        """ハッシュマップ（dict）のキーとして使用するためのハッシュ値。
        Java本と同様に、一旦 0 を返して動作を確認します。
        """
        return 0
