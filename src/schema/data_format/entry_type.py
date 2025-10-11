from datetime import date
from typing import TypedDict


class EntryType(TypedDict, total=True):  # total=Trueで必須項目にする
    """ジャーナルエントリの型定義"""

    date: date  # 日付
    number: int | None  # 日付が重複している場合のエントリ番号
    title: str  # タイトル
    body: str  # 本文


class ParserEntryType(TypedDict, total=True):
    """パースされたジャーナルエントリの型定義"""

    title: str  # タイトル
    body: str  # 本文
