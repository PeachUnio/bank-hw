import logging
from typing import Union

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/masks.log")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: Union[int]) -> Union[str]:
    """Функция, которая маскирует номер счета"""
    if card_number:
        logger.info(f"Маскирует номер карты {card_number}")
        str_card_number = str(card_number)
        masking_card_number = str_card_number[:4] + " " + str_card_number[4:6] + "** ****" + " " + str_card_number[12:]
        return masking_card_number
    logger.error("Не было передано номера карты")
    return ""


def get_mask_account(account: Union[int]) -> Union[str]:
    """Функция, которая маскирует номер акаунта"""
    logger.info(f"Маскирует номер cxtnf {account}")
    str_account = str(account)
    masking_account = "**" + str_account[-4:]
    return masking_account
