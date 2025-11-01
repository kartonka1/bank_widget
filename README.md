# Bank Widget

Проект "Bank Widget" предназначен для работы с банковскими операциями клиента. Он позволяет маскировать номера карт и счетов, а также обрабатывать и сортировать данные операций.

## Установка

Клонируйте репозиторий:

git clone https://github.com/kartonka1/bank_widget.git

Перейдите в папку проекта и создайте виртуальное окружение с помощью Poetry:

cd bank_widget
poetry install

Запустите проект:

poetry run python main.py


Функции
mask_account_card(data: str) -> str

Принимает строку с типом и номером карты или счёта и возвращает строку с замаскированным номером.


Примеры:

mask_account_card("Visa Platinum 7000792289606361")
# "Visa Platinum 7000 79** **** 6361"
mask_account_card("Счет 73654108430135874305")
# "Счет **4305"

get_date(date_str: str) -> str

Принимает дату в формате ISO 8601 ("2024-03-11T02:26:18.671407") и возвращает её в формате "ДД.ММ.ГГГГ".


Пример:
get_date("2024-03-11T02:26:18.671407")
# "11.03.2024"

get_mask_card_number(card_number: int) -> str
Возвращает замаскированный номер карты (используется в mask_account_card).

get_mask_account(account_number: int) -> str
Возвращает замаскированный номер счёта (используется в mask_account_card).

filter_by_state(operations: list[dict], state: str = "EXECUTED") -> list[dict]
Фильтрует список операций по значению ключа state. Возвращает новый список операций, удовлетворяющих условию.

sort_by_date(operations: list[dict], descending: bool = True) -> list[dict]
Сортирует список операций по дате. Параметр descending=True означает сортировку по убыванию (сначала самые последние операции).


Пример работы:

from src.widget import mask_account_card, get_date
from src.processing import filter_by_state, sort_by_date

# Маскировка карты и счёта
print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))

# Форматирование даты
print(get_date("2024-03-11T02:26:18.671407"))

# Работа с операциями
operations = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}
]

executed_ops = filter_by_state(operations)
sorted_ops = sort_by_date(operations)


Лицензия

Проект предоставляется "как есть", без каких-либо гарантий.