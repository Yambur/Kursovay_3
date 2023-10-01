import pytest
from src.utils import get_date, mask_prepare_message_number, mask_card_number, mask_account_number, filter_and_sorting


def test_get_date():
    assert get_date("2019-08-26T10:50:58.294041") == "26.08.2019"
    assert get_date("1234-56-78dsadsa") == "78.56.1234"
    assert get_date("--") >= ".."


def test_mask_prepare_message_number():
    assert mask_prepare_message_number("Счет 12345678") == "Счет **5678"
    assert mask_prepare_message_number(None) == "Личный счет"


def test_mask_card_number():
    assert mask_card_number("1234567890123456") == "1234 56** **** 3456"
    assert mask_card_number("1234567124463676576675463") == None


def test_mask_account_number():
    assert mask_account_number("12345") == "**2345"
    assert mask_account_number("1") == None


# скажем спасибо чату gpt за мои сохраненные нервы.......
def test_filter_and_sorting_with_executed_states():
    data = [
        {'state': 'PENDING', 'date': '2023-10-01'},
        {'state': 'EXECUTED', 'date': '2023-09-30'},
        {'state': 'EXECUTED', 'date': '2023-09-29'},
        {'state': 'PENDING', 'date': '2023-09-28'},
    ]

    expected_result = [
        {'state': 'EXECUTED', 'date': '2023-09-30'},
        {'state': 'EXECUTED', 'date': '2023-09-29'},
    ]

    result = filter_and_sorting(data)
    assert result == expected_result


def test_filter_and_sorting_no_executed_states():
    data = [
        {'state': 'PENDING', 'date': '2023-10-01'},
        {'state': 'CANCELLED', 'date': '2023-09-30'},
        {'state': 'PENDING', 'date': '2023-09-29'},
    ]

    expected_result = []

    result = filter_and_sorting(data)
    assert result == expected_result


def test_filter_and_sorting_empty_input():
    data = []

    expected_result = []

    result = filter_and_sorting(data)
    assert result == expected_result
