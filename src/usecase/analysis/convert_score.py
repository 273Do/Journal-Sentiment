from typing import Literal


def convert_to_5_scale(result: dict) -> Literal[1, 2, 3, 4, 5]:
    """transformersの結果を5段階評価に変換

    Args:
        result: transformersのpipeline結果
            - label: 'positive' or 'negative'
            - score: confidence (0.0-1.0)

    Returns:
        int: 1(非常にネガティブ) ~ 5(非常にポジティブ)

    変換ルール:
        - positive confidence >= 0.8: 5 (非常にポジティブ)
        - positive confidence >= 0.6: 4 (ポジティブ)
        - 0.4 < confidence < 0.6: 3 (中立)
        - negative confidence >= 0.6: 2 (ネガティブ)
        - negative confidence >= 0.8: 1 (非常にネガティブ)
    """
    label = result["label"].lower()
    score = result["score"]

    if "positive" in label:
        if score >= 0.8:
            return 5
        elif score >= 0.6:
            return 4
        else:
            return 3
    else:
        if score >= 0.8:
            return 1
        elif score >= 0.6:
            return 2
        else:
            return 3
