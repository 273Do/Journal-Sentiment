import pandas as pd

from src.schema.data_format.entry_type import EntryType
from src.usecase.data_format.read_html import read_html


def html_to_df(files: list[str]) -> pd.DataFrame:
    """HTMLからDataFrameに変換する関数

    Args:
        files: HTMLファイルのパスのリスト

    Returns:
        pd.DataFrame: カラム [date, title, body] を持つDataFrame
            - date: datetime.date
            - title: str
            - body: str
    """

    print("🚀 HTML から DataFrame への変換スクリプトを開始")

    # 全レコードを格納するリスト
    records: list[dict] = []

    # エントリのHTMLを読み込む
    for file in files:
        # htmlをパースしてEntryTypeに変換
        entry: EntryType = read_html(file)

        records.append(entry)

        # 全レコードからDataFrameを作成
        df: pd.DataFrame = pd.DataFrame(
            records, columns=list(EntryType.__annotations__.keys())
        )

        # 日付でdfをソート
        df_sorted = df.sort_values("date")

    return df_sorted
