import os

from dotenv import load_dotenv

from src.usecase.data_format.csv_to_df import csv_to_df

load_dotenv()

print("📖 解析用にデータを整形")

df = csv_to_df(os.getenv("OUTPUT_PATH") + "/entry.csv")
