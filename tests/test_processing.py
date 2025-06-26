import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def list_with_state():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

@pytest.fixture
def list_without_state():
    return [{'id': 41428829, 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'date': '2018-10-14T08:21:33.419441'}]

@pytest.fixture
def state_canceled():
    return [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

@pytest.fixture
def data_list():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

@pytest.fixture
def reverse_data_list():
    return [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]


def test_filter_by_state(list_with_state, list_without_state, state_canceled):
    assert filter_by_state(list_with_state) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
    assert filter_by_state(list_with_state, "CANCELED") == state_canceled
    assert filter_by_state(list_without_state) == list_without_state


def test_sort_by_date(data_list, reverse_data_list):
    assert sort_by_date(data_list) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                                       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
    assert sort_by_date(data_list,False) == reverse_data_list