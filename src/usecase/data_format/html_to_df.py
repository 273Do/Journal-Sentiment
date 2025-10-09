import glob

import pandas as pd


def html_to_df():
    """HTMLからDataFrameに変換する関数"""

    # dfの型を作成
    df = pd.DataFrame(
        columns=[
            "date",  # 日付
            "number",  # 番号
            "title",  # タイトル
            "entry",  # 本文
        ]
    ).astype(
        {
            "date": "datetime64[ns]",
            "number": "int64",
            "title": "string",
            "entry": "string",
        }
    )
    print(df)

    # AppleJournalEntries/EntriesのHTMLを読み込み、DataFrameに変換
    files = glob.glob("./tmp/*")

    for file in files:
        print(file)

    print("Converting HTML content to DataFrame")
