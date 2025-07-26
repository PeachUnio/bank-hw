import json
import logging
from json import JSONDecodeError

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/utils.log")
file_formatter = logging.Formatter(
    "%(asctime)s - %(filename)s - %(levelname)s: %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def load_transactions(file_path):
    """Функция принимает путь до JSON-файла и возвращает список транзакций"""
    try:
        logger.info(f"Открываем файл utilsпо пути {file_path}")
        with open(file_path, "r", encoding="utf-8") as file:
            json_data = json.load(file)
        if isinstance(json_data, list):
            logger.info("Возвращаем список транзакций из JSON-файла")
            return json_data
        else:
            logger.info("В файле не было списка")
            return []
    except JSONDecodeError:
        logger.error("Произошла ошибка JSONDecodeError")
        return []
    except TypeError:
        logger.error("Произошла ошибка TypeError")
        return []
    except FileNotFoundError:
        logger.error("Произошла ошибка FileNotFoundError")
        return []
