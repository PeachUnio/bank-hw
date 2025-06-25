from src.masks import get_mask_card_number, get_mask_account

def test_get_mask_card_number():
    assert get_mask_card_number(7000792289606361) == "7000 79** **** 6361"

    assert get_mask_card_number(7779077786666688886) == "7779 07** **** 6688886"

    assert get_mask_card_number("") == ""


def test_get_mask_account():
    assert get_mask_account(73654108430135874305) == "**4305"

    assert get_mask_account(48387853955938559393585853) == "**5853"

    assert get_mask_account(665798797) == "**8797"
