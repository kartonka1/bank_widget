import pytest

from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)


@pytest.fixture
def transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
    ]


@pytest.mark.parametrize(
    "currency, expected_count",
    [
        ("USD", 2),
        ("RUB", 1),
        ("EUR", 0),
    ],
)
def test_filter_by_currency(transactions, currency, expected_count):
    result = list(filter_by_currency(transactions, currency))
    assert len(result) == expected_count


def test_transaction_descriptions(transactions):
    gen = transaction_descriptions(transactions)
    result = list(gen)

    assert result == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
    ]


def test_transaction_descriptions_empty():
    gen = transaction_descriptions([])
    assert list(gen) == []


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (5, 5, ["0000 0000 0000 0005"]),
    ],
)
def test_card_number_generator_range(start, stop, expected):
    result = list(card_number_generator(start, stop))
    assert result == expected


def test_card_number_generator_format():
    gen = card_number_generator(1, 1)
    card = next(gen)

    parts = card.split(" ")
    assert len(parts) == 4
    assert all(len(part) == 4 for part in parts)
    assert card.replace(" ", "").isdigit()


def test_card_number_generator_large():
    gen = card_number_generator(9999, 10000)
    cards = list(gen)

    assert cards == [
        "0000 0000 0000 9999",
        "0000 0000 0001 0000",
    ]
