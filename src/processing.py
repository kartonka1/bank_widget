from typing import Any, Dict, List


def filter_by_state(operations: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Фильтрует список операций по заданному состоянию.

    :param operations: список словарей с данными операций
    :param state: значение для фильтрации по ключу 'state' (по умолчанию 'EXECUTED')
    :return: новый список, содержащий только операции с указанным state
    """
    return [op for op in operations if op.get("state") == state]


def sort_by_date(data: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список операций по дате.

    :param data: список словарей с ключом 'date'
    :param descending: порядок сортировки (по умолчанию — по убыванию)
    :return: новый список, отсортированный по дате
    :return: новый список, отсортированный по дате
    """
    return sorted(data, key=lambda x: x["date"], reverse=descending)
