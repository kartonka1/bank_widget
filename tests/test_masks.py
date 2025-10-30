import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    assert get_mask_card_number(1234567812345678) == "1234 56** **** 5678"
    with pytest.raises(ValueError):
        get_mask_card_number(123)  # слишком короткий номер


def test_get_mask_account():
    assert get_mask_account(9876543210) == "**3210"
    with pytest.raises(ValueError):
        get_mask_account(123)  # меньше 4 цифр
