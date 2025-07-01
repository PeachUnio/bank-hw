from typing import Union


def get_mask_card_number(card_number: Union[int]) -> Union[str]:
    """Функция, которая маскирует номер счета"""
    if card_number:
        str_card_number = str(card_number)
        masking_card_number = str_card_number[:4] + " " + str_card_number[4:6] + "** ****" + " " + str_card_number[12:]
        return masking_card_number
    return ""


def get_mask_account(account: Union[int]) -> Union[str]:
    """Функция, которая маскирует номер акаунта"""
    str_account = str(account)
    masking_account = "**" + str_account[-4:]
    return masking_account
