from typing import List, Dict


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


def sort_by_date(list_of_dict: List[Dict[str, str]], reverse: bool = True) -> List[Dict[str, str]]:
    """Функция сортирует список словарей по дате"""
    return sorted(list_of_dict, key=lambda i: i["date"], reverse=reverse)
