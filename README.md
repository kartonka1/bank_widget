# Bank Widget

Проект "Bank Widget" предназначен для работы с банковскими операциями клиента.  
Он позволяет маскировать номера карт и счетов, а также обрабатывать и сортировать данные операций.

---

## Установка

Клонируйте репозиторий:

```bash
git clone https://github.com/kartonka1/bank_widget.git
Перейдите в папку проекта и создайте виртуальное окружение с помощью Poetry:

bash
Копировать код
cd bank_widget
poetry install
Запустите проект:

bash
Копировать код
poetry run python main.py
Функции
mask_account_card(data: str) -> str
Принимает строку с типом и номером карты или счёта и возвращает строку с замаскированным номером.

Примеры:

python
Копировать код
mask_account_card("Visa Platinum 7000792289606361")
# "Visa Platinum 7000 79** **** 6361"

mask_account_card("Счет 73654108430135874305")
# "Счет **4305"
get_date(date_str: str) -> str
Принимает дату в формате ISO 8601 и возвращает её в формате "ДД.ММ.ГГГГ".

python
Копировать код
get_date("2024-03-11T02:26:18.671407")
# "11.03.2024"
get_mask_card_number(card_number: int) -> str
Маскирует номер карты.

get_mask_account(account_number: int) -> str
Маскирует номер счёта.

filter_by_state(operations: list[dict], state: str = "EXECUTED") -> list[dict]
Фильтрует операции по ключу state.

sort_by_date(operations: list[dict], descending: bool = True) -> list[dict]
Сортирует список операций по дате.

🧪 Тестирование
В проекте используется библиотека pytest для модульного тестирования
и pytest-cov для генерации отчётов покрытия.

Запуск тестов:
bash
Копировать код
poetry run pytest
Запуск тестов с покрытием:
bash
Копировать код
poetry run pytest --cov=src --cov-report=html
После выполнения появится папка:

bash
Копировать код
htmlcov/index.html
Открой этот файл в браузере, чтобы посмотреть отчёт о покрытии.

Покрытие тестами
Все функции проекта покрыты тестами:

masks.py

processing.py

widget.py

Итоговое тестовое покрытие: 100%

Лицензия
Проект предоставляется "как есть", без каких-либо гарантий.

yaml
Копировать код

---

### Готово! 