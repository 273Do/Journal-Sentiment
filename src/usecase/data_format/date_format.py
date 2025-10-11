from datetime import datetime


def date_format(date_str: str) -> datetime.date:
    """日付を"YYYY-MM-DD"形式の文字列に変換する関数

    例 2025年9月21日 日曜日-> 2025-09-21()

    Args:
        date: datetime.dateオブジェクト

    Returns:
        str: "YYYY-MM-DD"形式の文字列
    """

    formatted_date = datetime.strptime(date_str, "%Y年%m月%d日").date()
    return formatted_date.strftime("%Y-%m-%d")
