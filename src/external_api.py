import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("EXCHANGE_RATES_API_KEY")
API_URL = "https://api.apilayer.com/exchangerates_data/latest"


def convert_to_rubles(transaction: dict) -> float:
    amount = float(transaction.get("amount", 0))
    currency = transaction.get("currency", "RUB").upper()

    if currency == "RUB":
        return amount

    if currency not in ["USD", "EUR"]:
        raise ValueError(f"Конвертация для валюты {currency} не поддерживается.")

    headers = {"apikey": API_KEY}
    params = {
        "base": "RUB",
        "symbols": currency,
    }

    response = requests.get(API_URL, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()

    if "rates" not in data or currency not in data["rates"]:
        raise ValueError("API не вернул курс валют")

    rate = data["rates"][currency]  # сколько валюты за 1 RUB
    return amount / rate
