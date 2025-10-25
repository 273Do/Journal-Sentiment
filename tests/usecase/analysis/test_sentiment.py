from datetime import date
from unittest.mock import patch

import pandas as pd
import pytest

from src.usecase.analysis.sentiment import sentiment_analysis


@pytest.fixture
def sample_analysis_df():
    """テスト用のAnalysisDataTypeのDataFrameを作成"""
    return pd.DataFrame(
        [
            {
                "date": date(2024, 1, 1),
                "title": "良い日",
                "body": "今日はとても素晴らしい一日でした。",
                "titleCount": 3,
                "bodyCount": 17,
            },
            {
                "date": date(2024, 1, 2),
                "title": "悪い日",
                "body": "今日は最悪な一日でした。",
                "titleCount": 3,
                "bodyCount": 13,
            },
            {
                "date": date(2024, 1, 3),
                "title": "普通の日",
                "body": "特に何もない普通の日でした。",
                "titleCount": 4,
                "bodyCount": 15,
            },
        ]
    )


def test_sentiment_analysis_basic(sample_analysis_df):
    """基本的な感情分析のテスト"""
    with patch("src.usecase.analysis.sentiment.sentiment_pipeline") as mock_pipeline:
        # モックの返り値を設定
        mock_pipeline.side_effect = [
            [{"label": "POSITIVE", "score": 0.9}],  # 1行目
            [{"label": "NEGATIVE", "score": 0.9}],  # 2行目
            [{"label": "POSITIVE", "score": 0.5}],  # 3行目
        ]

        result = sentiment_analysis(sample_analysis_df)

        # sentimentScoreカラムが追加されている
        assert "sentimentScore" in result.columns

        # 各行のsentimentScoreが正しく設定されている
        assert result.iloc[0]["sentimentScore"] == 5  # positive, score=0.9 -> 5
        assert result.iloc[1]["sentimentScore"] == 1  # negative, score=0.9 -> 1
        assert result.iloc[2]["sentimentScore"] == 3  # positive, score=0.5 -> 3


def test_sentiment_analysis_columns_order(sample_analysis_df):
    """ResultDataTypeで定義された順序でカラムが並んでいることを確認"""
    with patch("src.usecase.analysis.sentiment.sentiment_pipeline") as mock_pipeline:
        mock_pipeline.side_effect = [
            [{"label": "POSITIVE", "score": 0.9}],
            [{"label": "NEGATIVE", "score": 0.9}],
            [{"label": "POSITIVE", "score": 0.5}],
        ]

        result = sentiment_analysis(sample_analysis_df)

        # 期待されるカラム順序
        expected_columns = [
            "date",
            "title",
            "body",
            "titleCount",
            "bodyCount",
            "sentimentScore",
        ]
        assert list(result.columns) == expected_columns


def test_sentiment_analysis_preserves_data(sample_analysis_df):
    """元のデータが保持されていることを確認"""
    with patch("src.usecase.analysis.sentiment.sentiment_pipeline") as mock_pipeline:
        mock_pipeline.side_effect = [
            [{"label": "POSITIVE", "score": 0.9}],
            [{"label": "NEGATIVE", "score": 0.9}],
            [{"label": "POSITIVE", "score": 0.5}],
        ]

        result = sentiment_analysis(sample_analysis_df)

        # 元のデータが保持されている
        assert result.iloc[0]["date"] == date(2024, 1, 1)
        assert result.iloc[0]["title"] == "良い日"
        assert result.iloc[0]["body"] == "今日はとても素晴らしい一日でした。"
        assert result.iloc[0]["titleCount"] == 3
        assert result.iloc[0]["bodyCount"] == 17


def test_sentiment_analysis_uses_body_text(sample_analysis_df):
    """bodyテキストを使って感情分析を行っていることを確認"""
    with patch("src.usecase.analysis.sentiment.sentiment_pipeline") as mock_pipeline:
        mock_pipeline.side_effect = [
            [{"label": "POSITIVE", "score": 0.9}],
            [{"label": "NEGATIVE", "score": 0.9}],
            [{"label": "POSITIVE", "score": 0.5}],
        ]

        sentiment_analysis(sample_analysis_df)

        # pipelineが各bodyテキストで呼ばれている
        assert mock_pipeline.call_count == 3
        mock_pipeline.assert_any_call("今日はとても素晴らしい一日でした。")
        mock_pipeline.assert_any_call("今日は最悪な一日でした。")
        mock_pipeline.assert_any_call("特に何もない普通の日でした。")


def test_sentiment_analysis_empty_dataframe():
    """空のDataFrameに対するテスト"""
    empty_df = pd.DataFrame(
        columns=["date", "title", "body", "titleCount", "bodyCount"]
    )

    with patch("src.usecase.analysis.sentiment.sentiment_pipeline") as mock_pipeline:
        result = sentiment_analysis(empty_df)

        # 空のDataFrameが返される
        assert len(result) == 0
        # カラムは正しく存在する
        assert "sentimentScore" in result.columns
        # pipelineは呼ばれない
        assert mock_pipeline.call_count == 0


def test_sentiment_analysis_single_row():
    """1行だけのDataFrameに対するテスト"""
    single_df = pd.DataFrame(
        [
            {
                "date": date(2024, 1, 1),
                "title": "テスト",
                "body": "テスト本文です。",
                "titleCount": 4,
                "bodyCount": 8,
            }
        ]
    )

    with patch("src.usecase.analysis.sentiment.sentiment_pipeline") as mock_pipeline:
        mock_pipeline.return_value = [{"label": "POSITIVE", "score": 0.8}]

        result = sentiment_analysis(single_df)

        # 1行のデータが返される
        assert len(result) == 1
        assert result.iloc[0]["sentimentScore"] == 5
        # pipelineが1回だけ呼ばれる
        assert mock_pipeline.call_count == 1
