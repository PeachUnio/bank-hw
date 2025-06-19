def filter_by_state(list_dict, my_state="EXECUTED"):
    """
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению
    """
    new_list = []
    for i in list_dict:
        if i["state"] == my_state:
            new_list.append(i)
    return new_list
