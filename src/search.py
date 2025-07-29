import re
from collections import defaultdict
from collections import Counter


def process_bank_search(data, search):
    """
    Фильтрует операции по строке поиска в описании
    """
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    return [op for op in data if "description" in op and pattern.search(op["description"])]


def process_bank_operations(data, categories):
    """Функция, которая подсчитывает кол-во операций в каждой категории"""
    new_dict = []
    patterns = {category: re.compile(re.escape(category), re.IGNORECASE)
                for category in categories}
    for op in data:
        if "description" not in op:
            continue
        description = op["description"]
        for category, pattern in patterns.items():
            if pattern.search(description):
                new_dict.append(category)
    return dict(Counter(new_dict))
