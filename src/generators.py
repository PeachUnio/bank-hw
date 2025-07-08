def filter_by_currency(transactions_list, currency):
    """
    Функция, которая поочередно выдает транзакции, где валюта операции соответствует заданной
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