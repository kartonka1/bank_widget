# Bank Widget

Проект **Bank Widget** предназначен для работы с банковскими операциями клиента.  
Он позволяет маскировать номера карт и счетов, фильтровать и сортировать транзакции,  
а также работать с большими массивами данных с помощью генераторов и декораторов.

---

## Установка

Клонируйте репозиторий:

```bash
git clone https://github.com/kartonka1/bank_widget.git
Перейдите в папку проекта и установите зависимости:

bash
Копировать код
cd bank_widget
poetry install
Запуск основного файла:

bash
Копировать код
poetry run python main.py
Основные функции проекта
mask_account_card(data: str) -> str
Принимает строку с типом и номером карты или счёта и возвращает замаскированный номер.

Примеры:

python
Копировать код
mask_account_card("Visa Platinum 7000792289606361")
# Visa Platinum 7000 79** **** 6361

mask_account_card("Счет 73654108430135874305")
# Счет **4305
get_date(date_str: str) -> str
Преобразует дату из ISO-формата в формат ДД.ММ.ГГГГ.

python
Копировать код
get_date("2024-03-11T02:26:18.671407")
# 11.03.2024
get_mask_card_number(card_number: int) -> str
Маскирует номер банковской карты.

get_mask_account(account_number: int) -> str
Маскирует номер банковского счёта.

filter_by_state(operations, state="EXECUTED")
Фильтрует операции по статусу.

sort_by_date(operations, reverse=True)
Сортирует операции по дате.

Модуль generators
Модуль содержит генераторы для обработки больших массивов транзакций.

filter_by_currency(transactions, currency)
Возвращает итератор транзакций с указанной валютой.

python
Копировать код
usd_transactions = filter_by_currency(transactions, "USD")
print(next(usd_transactions))
transaction_descriptions(transactions)
Генератор описаний операций.

python
Копировать код
for desc in transaction_descriptions(transactions):
    print(desc)
card_number_generator(start, stop)
Генератор номеров карт в формате:

nginx
Копировать код
XXXX XXXX XXXX XXXX
python
Копировать код
for number in card_number_generator(1, 5):
    print(number)
Модуль decorators
Модуль содержит декораторы для расширения функциональности функций.

log(filename: Optional[str] = None)
Декоратор логирует выполнение функции.

При успешном выполнении записывает имя функции и статус ok

При ошибке записывает имя функции, тип ошибки и входные параметры

Может писать лог в консоль или в файл

Логирование в консоль:
python
Копировать код
from src.decorators.log import log

@log()
def add(a, b):
    return a + b

add(1, 2)
# add ok
Логирование в файл:
python
Копировать код
@log(filename="app.log")
def multiply(a, b):
    return a * b

multiply(2, 3)
# Запись в app.log: multiply ok
Обработка ошибок:
python
Копировать код
@log()
def divide(a, b):
    return a / b

divide(1, 0)
# divide error: ZeroDivisionError. Inputs: (1, 0), {}
Тестирование
В проекте используется pytest.

Все функции покрыты тестами, включая:

успешные сценарии

обработку ошибок

Покрытие тестами: 100%

HTML-отчёт о покрытии тестами находится в папке htmlcov.

Покрытые модули:

masks.py

processing.py

widget.py

generators.py

decorators/log.py

Лицензия
Проект предоставляется «как есть», без каких-либо гарантий.