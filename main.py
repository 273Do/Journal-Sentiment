import os
import sys

from dotenv import load_dotenv

from src.usecase.analysis.sentiment import sentiment_analysis
from src.usecase.data_format.csv_to_df import csv_to_df

load_dotenv()

args = sys.argv

start_date = args[1]
end_date = args[2]

print(start_date, end_date)

print("=" * 50)
print("🚀 感情分析処理を開始")

# 解析用にデータを整形
analysis_df = csv_to_df(os.getenv("OUTPUT_PATH") + "/entry.csv")

# 感情評価データを出力
sentiment_df = sentiment_analysis(analysis_df)

# 月別感情分布(5段階)を解析
print("📊 月別感情分布(5段階)を解析中...")
# TODO: 実装予定

print("=" * 50)
print("✨ 全ての処理が完了しました")
print("=" * 50)
