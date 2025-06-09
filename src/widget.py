from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_accaunt_number: Union[str]) -> Union[str]:
    if "Счет" in card_accaunt_number:
        account_number = card_accaunt_number[5:]
        mask_accunt = get_mask_account(account_number)
        return f"{card_accaunt_number[:4]} {mask_accunt}"
    else:
        card_number = card_accaunt_number[-16:]
        card_name = card_accaunt_number[:-17]
        mask_card = get_mask_card_number(card_number)
        return f"{card_name} {mask_card}"


def get_date(data: Union[str]) -> Union[str]:
    """Функция, которая преобразует дату"""
    day = data[8:10]
    month = data[5:7]
    year = data[:4]
    return f"{day}.{month}.{year}"
