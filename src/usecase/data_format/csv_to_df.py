import pandas as pd

from src.schema.analysis.analysis_data_type import AnalysisDataType


def csv_to_df(file: str) -> pd.DataFrame:
    """CSVからDataFrameに変換する関数

    Args:
        file: CSVファイルのパス

    Returns:
        pd.DataFrame: カラム AnalysisDataType を持つDataFrame
            - date: datetime.date
            - title: str
            - body: str
            - titleCount: int
            - bodyCount: int
    """

    print("\n📖 解析用にデータを整形中...")

    # CSVを読み込む
    df: pd.DataFrame = pd.read_csv(file)

    # titleCountとbodyCountカラムを追加
    df["titleCount"] = df["title"].str.len()
    df["bodyCount"] = df["body"].str.len()

    # AnalysisDataTypeで定義されたカラム順に並び替え
    columns = list(AnalysisDataType.__annotations__.keys())
    df = df[columns]

    return df
