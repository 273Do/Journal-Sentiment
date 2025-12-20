import os
from datetime import datetime

import pandas as pd


def check_date(selected_start: int, selected_end: int, min_date: int, max_date: int):
    """入力された日付が正しい日付かチェック

    Args:
        selected_start: 選択された開始日
        selected_end: 選択された終了日
        min_date: データの最小日付
        max_date: データの最大日付

    Returns:
        _type_: _description_
    """

    # データの範囲を取得
    entry_df = pd.read_csv(os.getenv("OUTPUT_PATH") + "/entry.csv")
    entry_df["date"] = pd.to_datetime(entry_df["date"], format="%Y-%m-%d")
    min_date = entry_df["date"].min().strftime("%Y%m%d")
    max_date = entry_df["date"].max().strftime("%Y%m%d")

    # 日付形式のチェック
    try:
        start_date = datetime.strptime(selected_start, "%Y%m%d")
        end_date = datetime.strptime(selected_end, "%Y%m%d")
    except ValueError:
        raise ValueError("日付はYYYYMMDD形式で入力してください。")

    # データの範囲内かチェック
    if selected_start < min_date or selected_end > max_date:
        raise ValueError(
            f"日付はデータの範囲内で指定してください。範囲: {min_date} - {max_date}"
        )

    if start_date > end_date:
        raise ValueError("開始日は終了日より前の日付を指定してください。")

    return selected_start, selected_end
