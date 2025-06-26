import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card, masks_number",
    [(7000792289606361, "7000 79** **** 6361"), (7779077786666688886, "7779 07** **** 6688886"), ("", "")],
)
def test_get_mask_card_number(card: int, masks_number: str) -> None:
    assert get_mask_card_number(card) == masks_number


@pytest.mark.parametrize(
    "account, masks_account",
    [(73654108430135874305, "**4305"), (48387853955938559393585853, "**5853"), (665798797, "**8797")],
)
def test_get_mask_account(account: int, masks_account: str) -> None:
    assert get_mask_account(account) == masks_account
