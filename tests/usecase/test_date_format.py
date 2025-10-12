from datetime import date

from src.usecase.data_format.date_format import date_format


def test_date_format():
    assert date_format("2024年9月17日 火曜日") == date(2024, 9, 17)
    assert date_format("2024年10月5日 土曜日") == date(2024, 10, 5)
    assert date_format("2024年12月31日 火曜日") == date(2024, 12, 31)
    assert date_format("2024年1月1日 月曜日") == date(2024, 1, 1)
    assert date_format("2024年11月9日 土曜日") == date(2024, 11, 9)
