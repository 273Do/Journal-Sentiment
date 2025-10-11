import os
from datetime import datetime

import pandas as pd

from src.schema.data_format.entry_type import EntryType, ParserEntryType
from src.usecase.data_format.read_html import read_html


def html_to_df(files: list[str]) -> pd.DataFrame:
    """HTMLからDataFrameに変換する関数

    Args:
        files: HTMLファイルのパスのリスト

    Returns:
        pd.DataFrame: カラム [date, number, title, body] を持つDataFrame
            - date: datetime.date
            - number: int
            - title: str
            - body: str
    """

    # 全レコードを格納するリスト
    records: list[dict] = []

    # エントリのHTMLを読み込む
    for file in files:
        # htmlをパース
        entry: ParserEntryType = read_html(file)

        # ファイル名から日付を抽出
        filename: str = os.path.basename(file)
        date_str: str = filename[:10]
        date: datetime = datetime.strptime(date_str, "%Y-%m-%d").date()

        # レコードに登録
        record: EntryType = {
            "date": date,
            "number": None,  # いらないか
            **entry,
        }

        records.append(record)

        # 全レコードからDataFrameを作成
        df: pd.DataFrame = pd.DataFrame(
            records, columns=list(EntryType.__annotations__.keys())
        )

        # 日付でdfをソート
        df_sorted = df.sort_values("date")

    return df_sorted
