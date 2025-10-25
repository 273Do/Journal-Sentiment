from typing import Literal, TypedDict

from src.schema.data_format.entry_type import EntryType


class SentimentResult(TypedDict):
    """感情分析の結果データの型"""

    label: str
    score: float


class AnalysisDataType(EntryType):
    """解析用データの型定義

    EntryTypeを継承し、titleCount, bodyCountフィールドを追加
    """

    titleCount: int  # タイトルの文字数
    bodyCount: int  # 本文の文字数


class ResultDataType(AnalysisDataType):
    """解析結果用データの型定義

    AnalysisDataTypeを継承し、sentimentScoreフィールドを追加
    negative: 1
    neutral: 3
    positive: 5
    """

    sentimentScore: Literal[1, 2, 3, 4, 5]  # 5 段階感情
