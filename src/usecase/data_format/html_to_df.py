import glob
import os
import sys

import pandas as pd
from dotenv import load_dotenv

from src.schema.data_format.entry_type import EntryType
from src.usecase.data_format.read_html import read_html

load_dotenv()


def html_to_df():
    """HTMLからDataFrameに変換する関数"""

    # dfの型を作成
    df: pd.DataFrame = pd.DataFrame(columns=[EntryType])

    print(df)

    # AppleJournalEntries/EntriesのHTMLを読み込み、DataFrameに変換
    files: list[str] = glob.glob(os.getenv("ENTRY_PATH") + "/*.html")

    for file in files:
        entry = read_html(file)
        print(entry)
        sys.exit()
