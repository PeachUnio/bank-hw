import json
from json import JSONDecodeError


def load_transactions(file_path):
    """Функция принимает путь до JSON-файла и возвращает список транзакций"""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            json_data = json.load(file)
        if isinstance(json_data, list):
            return json_data
        else:
            return []
    except JSONDecodeError:
        return []
    except TypeError:
        return []
    except FileNotFoundError:
        return []
