import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "card_account, mask_number",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 35383033474447895560", "Счет **5560"),
    ],
)
def test_mask_account_card(card_account: str, mask_number: str) -> None:
    assert mask_account_card(card_account) == mask_number


def test_get_date() -> None:
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"

    assert get_date("2000-11-06T02:26:18.671407") == "06.11.2000"
    assert get_date("") == ""
