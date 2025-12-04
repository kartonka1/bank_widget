from typing import Any, Dict, Iterator, List


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]:
    """
    Возвращает итератор по транзакциям, где валюта совпадает с переданной.
    """
    for tx in transactions:
        tx_currency = tx.get("operationAmount", {}).get("currency", {}).get("code")
        if tx_currency == currency:
            yield tx


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """
    Генератор, который по очереди возвращает описания транзакций.
    """
    for tx in transactions:
        desc = tx.get("description")
        if desc is not None:
            yield desc


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генератор номеров банковских карт.
    Выдаёт номера в формате XXXX XXXX XXXX XXXX в диапазоне [start, stop].
    """
    for number in range(start, stop + 1):
        # Преобразуем число в строку с ведущими нулями (16 цифр)
        num_str = f"{number:016d}"
        formatted = f"{num_str[0:4]} {num_str[4:8]} {num_str[8:12]} {num_str[12:16]}"
        yield formatted
