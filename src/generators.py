def filter_by_currency(transactions_list, currency):
    """
    Генератор, который поочередно выдает транзакции, где валюта операции соответствует заданной
    """
    found = False
    if transactions_list:
        for i in transactions_list:
            try:
               if i["operationAmount"]["currency"]["name"] == currency:
                   found = True
                   yield i
            except KeyError:
                yield []
    else:
        yield transactions_list
    if not found:
        yield []

def transaction_descriptions(transactions):
    """ГенеоаторБ который выдает описание функции"""
    found = False
    if transactions:
        for i in transactions:
            try:
                yield i["description"]
            except KeyError:
                yield []
    else:
        yield []
    if not found:
        yield []
