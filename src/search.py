import re


def process_bank_search(data, search):
    """
    Фильтрует операции по строке поиска в описании (с использованием regex)
    """
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    return [op for op in data if 'description' in op and pattern.search(op['description'])]
