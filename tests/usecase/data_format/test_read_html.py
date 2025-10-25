from datetime import date
from pathlib import Path

from src.usecase.data_format.read_html import read_html

from .test_html_to_df import sample_html_pattern1, sample_html_pattern2  # noqa: F401


def test_read_html_pattern1(sample_html_pattern1: str):  # noqa: F811
    """パターン1のHTMLを正しくパースできることを確認"""
    # 実行
    result = read_html(sample_html_pattern1)

    # 検証
    assert result["date"] == date(2024, 9, 17)
    assert result["title"] == "今日の振り返り"
    assert result["body"] == "今日も何もない1日だった。"


def test_read_html_pattern2(sample_html_pattern2: str):  # noqa: F811
    """パターン2のHTMLを正しくパースできることを確認"""
    # 実行
    result = read_html(sample_html_pattern2)

    # 検証
    assert result["date"] == date(2024, 10, 15)
    assert result["title"] == "今日の振り返り"
    assert result["body"] == "今日はいいお天気だった。"


def test_read_html_with_no_title(tmp_path: Path):
    """タイトルがない場合でも正しく処理できることを確認"""

    html_content = """
    <!DOCTYPE html>
    <html>
        <body>
            <div class="pageHeader">2024年11月1日 金曜日</div>
            <span class="s3">本文だけのエントリ。</span>
        </body>
    </html>
    """

    file_path = tmp_path / "no_title.html"
    file_path.write_text(html_content, encoding="utf-8")

    # 実行
    result = read_html(str(file_path))

    # 検証
    assert result["date"] == date(2024, 11, 1)
    assert result["title"] is None
    assert result["body"] == "本文だけのエントリ。"


def test_read_html_with_no_body(tmp_path: Path):
    """本文がない場合でも正しく処理できることを確認"""
    html_content = """
    <!DOCTYPE html>
    <html>
        <body>
            <div class="pageHeader">2024年12月25日 水曜日</div>
            <span class="s2">タイトルのみ</span>
        </body>
    </html>
    """

    file_path = tmp_path / "no_body.html"
    file_path.write_text(html_content, encoding="utf-8")

    # 実行
    result = read_html(str(file_path))

    # 検証
    assert result["date"] == date(2024, 12, 25)
    assert result["title"] == "タイトルのみ"
    assert result["body"] is None


def test_read_html_empty_file(tmp_path: Path):
    """空のHTMLファイルを処理できることを確認"""
    html_content = """
    <!DOCTYPE html>
    <html>
        <body>
        </body>
    </html>
    """

    file_path = tmp_path / "empty.html"
    file_path.write_text(html_content, encoding="utf-8")

    # 実行
    result = read_html(str(file_path))

    # 検証
    assert result["date"] is None
    assert result["title"] is None
    assert result["body"] is None
