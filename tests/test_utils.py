from src.utils import get_date, filter_and_sorting


def test_get_date():
    assert get_date("2019-08-26T10:50:58.294041") >= "2019-08-26"

