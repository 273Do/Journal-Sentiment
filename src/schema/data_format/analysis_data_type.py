from datetime import date
from typing import Literal, TypedDict


class AnalysisDataType(TypedDict, total=True):
    """解析用データの型定義"""

    date: date  # 日付
    title: str  # タイトル
    body: str  # 本文
    titleCount: int  # タイトルの文字数
    bodyCount: int  # 本文の文字数


class ResultDataType(TypedDict, total=True):
    """解析結果用データの型定義"""

    date: date  # 日付
    title: str  # タイトル
    body: str  # 本文
    titleCount: int  # タイトルの文字数
    bodyCount: int  # 本文の文字数
    sentiment: Literal[1, 2, 3, 4, 5]  # 5 段階感情
