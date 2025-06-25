from src.widget import mask_account_card, get_date


def test_mask_account_card():
    assert mask_account_card("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert mask_account_card("Visa Platinum 8990922113665229") == "Visa Platinum 8990 92** **** 5229"

    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"
    assert mask_account_card("Счет 35383033474447895560") == "Счет **5560"

def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"

    assert get_date("2000-11-06T02:26:18.671407") == "06.11.2000"
    assert get_date("") == ""
