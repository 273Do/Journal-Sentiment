from pathlib import Path

import pandas as pd
import pytest

from src.usecase.data_format.csv_to_df import csv_to_df


@pytest.fixture
def sample_csv(tmp_path: Path) -> str:
    """サンプルCSVファイルを作成

    Args:
        tmp_path: pytestが提供する一時ディレクトリ

    Returns:
        str: 作成したCSVファイルのパス
    """

    csv_content = """date,title,body
2024-09-17,今日の振り返り,今日も何もない1日だった。
2024-10-15,今日の出来事,今日はいいお天気だった。
2024-10-16,日記,充実した1日だった。"""

    file_path = tmp_path / "test_entry.csv"
    file_path.write_text(csv_content, encoding="utf-8")
    return str(file_path)


def test_csv_to_df_columns(sample_csv: str):
    """CSVをDataFrameに変換し、正しいカラムが含まれているかテスト"""

    df = csv_to_df(sample_csv)

    # 検証: DataFrameが返されること
    assert isinstance(df, pd.DataFrame)

    # 検証: 正しいカラムが含まれていること
    expected_columns = ["date", "title", "body", "titleCount", "bodyCount"]
    assert list(df.columns) == expected_columns

    # 検証: 3行のデータが含まれていること
    assert len(df) == 3

    # 検証: titleCountが正しく計算されていること
    assert df.iloc[0]["titleCount"] == len("今日の振り返り")  # 7文字
    assert df.iloc[1]["titleCount"] == len("今日の出来事")  # 6文字
    assert df.iloc[2]["titleCount"] == len("日記")  # 2文字

    # 検証: bodyCountが正しく計算されていること
    assert df.iloc[0]["bodyCount"] == len("今日も何もない1日だった。")  # 13文字
    assert df.iloc[1]["bodyCount"] == len("今日はいいお天気だった。")  # 13文字
    assert df.iloc[2]["bodyCount"] == len("充実した1日だった。")  # 10文字

    # 検証: 1行目のデータ
    row0 = df.iloc[0]
    assert row0["date"] == "2024-09-17"
    assert row0["title"] == "今日の振り返り"
    assert row0["body"] == "今日も何もない1日だった。"

    # 検証: 2行目のデータ
    row1 = df.iloc[1]
    assert row1["date"] == "2024-10-15"
    assert row1["title"] == "今日の出来事"
    assert row1["body"] == "今日はいいお天気だった。"


def test_csv_to_df_empty_csv(tmp_path: Path):
    """空のCSVファイルを渡した場合のテスト"""
    # ヘッダーのみのCSVを作成
    csv_content = "date,title,body"
    file_path = tmp_path / "empty.csv"
    file_path.write_text(csv_content, encoding="utf-8")

    df = csv_to_df(str(file_path))

    # 検証: DataFrameが返されること
    assert isinstance(df, pd.DataFrame)

    # 検証: 行数が0であること
    assert len(df) == 0

    # 検証: カラムが正しく含まれていること
    expected_columns = ["date", "title", "body", "titleCount", "bodyCount"]
    assert list(df.columns) == expected_columns


def test_csv_to_df_nonexistent_file():
    """存在しないファイルを渡した場合のテスト"""
    # 実行と検証: FileNotFoundErrorが発生すること
    with pytest.raises(FileNotFoundError):
        csv_to_df("/nonexistent/path/to/file.csv")
