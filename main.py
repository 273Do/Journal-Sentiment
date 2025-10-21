import os

from dotenv import load_dotenv

from src.usecase.analysis.sentiment import sentiment_analysis
from src.usecase.data_format.csv_to_df import csv_to_df

load_dotenv()

# 解析用にデータを整形
analysis_df = csv_to_df(os.getenv("OUTPUT_PATH") + "/entry.csv")

# 感情評価データを出力
sentiment_df = sentiment_analysis(analysis_df)

# 月別感情分布(5段階)を解析


print("====== 月別感情分布(5段階)を解析 ======")
print("====== 月別感情バランス(5段階)を解析 ======")
