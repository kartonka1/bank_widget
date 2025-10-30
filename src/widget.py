from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """
    Принимает строку с типом и номером карты или счета.
    Маскирует номер с помощью функций из masks.py.
    """
    if data.startswith("Счет"):
        # Работаем со счётом
        parts = data.split()
        account_number = int(parts[-1])
        masked = get_mask_account(account_number)
        return f"Счет {masked}"
    else:
        # Работаем с картой
        *name_parts, card_number = data.split()
        card_name = " ".join(name_parts)
        masked = get_mask_card_number(int(card_number))
        return f"{card_name} {masked}"


def get_date(date_str: str) -> str:
    """
    Принимает дату в формате '2024-03-11T02:26:18.671407'
    и возвращает её в формате '11.03.2024'.
    """
    date_obj = datetime.fromisoformat(date_str)
    return date_obj.strftime("%d.%m.%Y")
