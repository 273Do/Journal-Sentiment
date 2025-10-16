import glob
import os

from dotenv import load_dotenv

from src.usecase.data_format.html_to_df import html_to_df

load_dotenv()

# エントリのHTMLファイルを取得
files: list[str] = glob.glob(os.getenv("ENTRY_PATH") + "/*.html")

# HTML から DataFrame への変換
df = html_to_df(files)

# データをcsvに出力
print("💾 データをcsvに出力")

df.to_csv(os.getenv("OUTPUT_PATH") + "/entry.csv")
