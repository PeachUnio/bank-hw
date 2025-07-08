from os import access

import pytest

from src.generators import filter_by_currency

@pytest.fixture
def transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 789769570,
            "state": "EXECUTED",
            "date": "2019-11-25T02:10:09.492572",
            "operationAmount": {
                "amount": "5428.78",
                "currency": {
                    "name": "EUR",
                    "code": "EUR"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 35383033474447895560",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 790064268,
            "state": "CANCELED",
            "date": "2017-03-04T13:44:05.206878",
            "operationAmount": {
                "amount": "6653.99",
                "currency": {
                    "name": "EUR",
                    "code": "EUR"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 35383033474447895560",
            "to": "Счет 7563538303347444"
        }
]

@pytest.fixture
def transactions_usd():
    return {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }


def test_filter_by_currency(transactions, transactions_usd):
    generator = filter_by_currency([], "USD")
    assert next(generator) == []
    generator = filter_by_currency(transactions, "CAD")
    assert next(generator) == []
    generator = filter_by_currency(transactions, "USD")
    assert next(generator) == transactions_usd
