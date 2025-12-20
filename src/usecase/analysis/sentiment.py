import os

import pandas as pd
from dotenv import load_dotenv
from transformers import pipeline

from src.schema.analysis.analysis_data_type import ResultDataType, SentimentResult
from src.usecase.analysis.convert_score import convert_to_5_scale

load_dotenv()

# 日本語感情分析モデル（positive/negative）
# 日本語に特化したBERTモデルを使用
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    # TODO: 環境変数で指定
    model=os.getenv("BERT"),
)


def sentiment_analysis(analysis_df: pd.DataFrame) -> pd.DataFrame:
    """解析用のdfのレコードを参照して感情分析を行う関数

    Args:
        pd.DataFrame: カラム AnalysisDataType を持つDataFrame
            - date: datetime.date
            - title: str
            - body: str
            - titleCount: int
            - bodyCount: int

    Returns:
        pd.DataFrame: カラム ResultDataType を持つDataFrame
            - date: datetime.date
            - title: str
            - body: str
            - titleCount: int
            - bodyCount: int
            - sentiment: int
    """

    print("🧪 感情分析を実行中...")

    total = len(analysis_df.index)
    sentiments = []

    # 1日ずつ感情分析を実施
    for i, entry in analysis_df.iterrows():
        text = entry["body"]

        # スコアを格納
        result: SentimentResult = sentiment_pipeline(text)[0]
        sentiment_score = convert_to_5_scale(result)
        sentiments.append(sentiment_score)

        progress = int((i + 1) / total * 100)
        print(f"\r進捗: {progress}% ({i + 1}/{total})", end="", flush=True)

    analysis_df["sentimentScore"] = sentiments

    # ResultDataTypeで定義されたカラム順に並び替え
    columns = list(ResultDataType.__annotations__.keys())
    result_df = analysis_df[columns]

    return result_df
