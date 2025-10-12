from datetime import date
from typing import TypedDict


class EntryType(TypedDict, total=True):  # total=Trueで必須項目にする
    """ジャーナルエントリの型定義"""

    date: date  # 日付
    title: str  # タイトル
    body: str  # 本文
