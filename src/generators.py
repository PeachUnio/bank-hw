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
    """Генеоатор, который выдает описание функции"""
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


def card_number_generator(start=1, stop=9999999999999999):
    """Генератор номеров для карт"""
    for number in range(start, stop + 1):
        number_of_zeros = 16 - len(str(number))
        card_number = f"{"0" * number_of_zeros}{number}"
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
