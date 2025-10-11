from datetime import date
from pathlib import Path

import pandas as pd
import pytest

from src.usecase.data_format.html_to_df import html_to_df


@pytest.fixture  # フィクスチャ(テストの前処理)を定義
def sample_html_pattern1(tmp_path: Path) -> str:
    """パターン1のサンプルHTMLファイルを作成

    パターン1: <div class='title'> + <span class="s2">(本文)
    """

    html_content = """
    <!DOCTYPE html>
    <html>
      <head>
        <title>Test</title>
      </head>
      <body>
        <div class="pageHeader">2024年9月17日 火曜日</div>
        <div class='title'>今日の振り返り</div>
        <span class="s2">今日も何もない1日だった。</span>
      </body>
    </html>
    """

    file_path = tmp_path / "2024-09-17_test.html"
    file_path.write_text(html_content, encoding="utf-8")
    return str(file_path)


@pytest.fixture
def sample_html_pattern2(tmp_path: Path) -> str:
    """パターン2のサンプルHTMLファイルを作成

    パターン2: <span class="s2">(タイトル) + <span class="s3">(本文)
    """
    html_content = """
    <!DOCTYPE html>
    <html>
      <head>
        <title>Test</title>
      </head>
      <body>
        <div class="pageHeader">2024年10月15日 水曜日</div>
        <span class="s2">今日の振り返り</span>
        <span class="s3">今日はいいお天気だった。</span>
      </body>
    </html>
    """

    file_path = tmp_path / "2024-10-15_test.html"
    file_path.write_text(html_content, encoding="utf-8")
    return str(file_path)


def test_html_to_df_pattern1(sample_html_pattern1: str):  # 引数にフィクスチャを指定
    """パターン1のHTMLファイルをDataFrameに変換するテスト"""
    # 実行
    df = html_to_df([sample_html_pattern1])

    # 検証
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1
    assert list(df.columns) == ["date", "title", "body"]

    # データの内容を検証
    row = df.iloc[0]
    assert row["date"] == date(2024, 9, 17)
    assert row["title"] == "今日の振り返り"
    assert row["body"] == "今日も何もない1日だった。"


def test_html_to_df_pattern2(sample_html_pattern2: str):
    """パターン2のHTMLファイルをDataFrameに変換するテスト"""
    # 実行
    df = html_to_df([sample_html_pattern2])

    # 検証
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1
    assert list(df.columns) == ["date", "title", "body"]

    # データの内容を検証
    row = df.iloc[0]
    assert row["date"] == date(2024, 10, 15)
    assert row["title"] == "今日の振り返り"
    assert row["body"] == "今日はいいお天気だった。"


def test_html_to_df_multiple_files(
    sample_html_pattern1: str, sample_html_pattern2: str
):
    """複数のHTMLファイルをDataFrameに変換するテスト"""
    # 実行
    df = html_to_df([sample_html_pattern1, sample_html_pattern2])

    # 検証
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2

    # 日付でソートされているか確認
    assert df.iloc[0]["date"] == date(2024, 9, 17)
    assert df.iloc[1]["date"] == date(2024, 10, 15)


def test_html_to_df_empty_list():
    """空のリストを渡した場合のテスト"""
    # 実行と検証
    with pytest.raises(Exception):
        html_to_df([])
