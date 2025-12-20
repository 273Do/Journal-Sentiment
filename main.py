import os
import sys

from dotenv import load_dotenv

from src.usecase.analysis.sentiment import sentiment_analysis
from src.usecase.data_format.csv_to_df import csv_to_df

load_dotenv()

args = sys.argv

selected_start = args[1]
selected_end = args[2]
min_date = args[3]
max_date = args[4]

# 入力された日付が正しい日付かチェック(YYYYMMDD形式、データの範囲かどうかチェック)
# [start_date, end_date] = check_date(selected_start, selected_end, min_date, max_date)

print("=" * 50)
print("🚀 感情分析処理を開始")

# 解析用にデータを整形
analysis_df = csv_to_df(os.getenv("OUTPUT_PATH") + "/entry.csv")

# 感情評価データを出力
sentiment_df = sentiment_analysis(
    analysis_df,
    # start_date, end_date
)
sentiment_df.to_csv(os.getenv("OUTPUT_PATH") + "/sentiment_entry.csv")

# 月別感情分布(5段階)を解析
print("📊 月別感情分布(5段階)を解析中...")
# TODO: 実装予定

print("=" * 50)
print("✨ 全ての処理が完了しました")
print("=" * 50)
