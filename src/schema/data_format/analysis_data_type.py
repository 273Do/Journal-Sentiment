from typing import Literal

from src.schema.data_format.entry_type import EntryType


class AnalysisDataType(EntryType):
    """解析用データの型定義

    EntryTypeを継承し、titleCount, bodyCountフィールドを追加
    """

    titleCount: int  # タイトルの文字数
    bodyCount: int  # 本文の文字数


class ResultDataType(AnalysisDataType):
    """解析結果用データの型定義

    AnalysisDataTypeを継承し、sentimentフィールドを追加
    """

    sentiment: Literal[1, 2, 3, 4, 5]  # 5 段階感情
