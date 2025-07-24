import os

import requests
from dotenv import load_dotenv
from requests import RequestException

load_dotenv()


def converting_transaction_into_rub(transaction):
    """Функция принимает на вход транзакцию и возвращает ее сумму.
    Если транзакция была в EUR или USD происходит обращение к внешнему API для выяснения курса валюты"""
    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]
    if currency == "RUB":
        return float(amount)
    api_key = os.getenv("API_KEY")
    url = "https://api.apilayer.com/exchangerates_data/convert"
    params = {"to": "RUB", "from": currency, "amount": amount}
    headers = {"apikey": api_key}
    try:
        r = requests.get(url, headers=headers, params=params)
        r.raise_for_status()
        data = r.json()
        return float(data["result"])
    except KeyError:
        return []
    except RequestException:
        return []
