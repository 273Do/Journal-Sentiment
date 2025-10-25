from src.usecase.analysis.convert_score import convert_to_5_scale


def test_convert_score_positive_very_high():
    """Positiveでconfidence >= 0.8の場合、5を返す"""
    result = {"label": "POSITIVE", "score": 0.9}
    assert convert_to_5_scale(result) == 5


def test_convert_score_positive_boundary_high():
    """Positiveでconfidenceがちょうど0.8の場合、5を返す"""
    result = {"label": "POSITIVE", "score": 0.8}
    assert convert_to_5_scale(result) == 5


def test_convert_score_positive_moderate():
    """Positiveでconfidence >= 0.6 かつ < 0.8の場合、4を返す"""
    result = {"label": "POSITIVE", "score": 0.7}
    assert convert_to_5_scale(result) == 4


def test_convert_score_positive_boundary_moderate():
    """Positiveでconfidenceがちょうど0.6の場合、4を返す"""
    result = {"label": "POSITIVE", "score": 0.6}
    assert convert_to_5_scale(result) == 4


def test_convert_score_positive_neutral():
    """Positiveでconfidence < 0.6の場合、3を返す"""
    result = {"label": "POSITIVE", "score": 0.5}
    assert convert_to_5_scale(result) == 3


def test_convert_score_negative_very_high():
    """Negativeでconfidence >= 0.8の場合、1を返す"""
    result = {"label": "NEGATIVE", "score": 0.9}
    assert convert_to_5_scale(result) == 1


def test_convert_score_negative_boundary_high():
    """Negativeでconfidenceがちょうど0.8の場合、1を返す"""
    result = {"label": "NEGATIVE", "score": 0.8}
    assert convert_to_5_scale(result) == 1


def test_convert_score_negative_moderate():
    """Negativeでconfidence >= 0.6 かつ < 0.8の場合、2を返す"""
    result = {"label": "NEGATIVE", "score": 0.7}
    assert convert_to_5_scale(result) == 2


def test_convert_score_negative_boundary_moderate():
    """Negativeでconfidenceがちょうど0.6の場合、2を返す"""
    result = {"label": "NEGATIVE", "score": 0.6}
    assert convert_to_5_scale(result) == 2


def test_convert_score_negative_neutral():
    """Negativeでconfidence < 0.6の場合、3を返す"""
    result = {"label": "NEGATIVE", "score": 0.5}
    assert convert_to_5_scale(result) == 3


def test_convert_score_case_insensitive():
    """labelは大文字小文字を区別しない"""
    result_lower = {"label": "positive", "score": 0.9}
    result_upper = {"label": "POSITIVE", "score": 0.9}
    result_mixed = {"label": "Positive", "score": 0.9}
    assert convert_to_5_scale(result_lower) == 5
    assert convert_to_5_scale(result_upper) == 5
    assert convert_to_5_scale(result_mixed) == 5
