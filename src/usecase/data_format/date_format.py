from datetime import datetime


def date_format(date_str: str) -> datetime.date:
    """日付文字列をdateオブジェクトに変換する関数

    Args:
        date_str: "YYYY年MM月DD日 曜日" 形式の日付文字列（例: "2025年9月21日 日曜日"）

    Returns:
        datetime.date: 日付オブジェクト
    """
    slice_week: str = date_str.split(" ")[0]
    return datetime.strptime(slice_week, "%Y年%m月%d日").date()
