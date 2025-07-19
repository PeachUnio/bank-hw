import json
import unittest
from src.external_api import converting_transaction_into_rub
from unittest.mock import Mock, patch, mock_open
from requests import RequestException


class TestLoadTransactions(unittest.TestCase):

    @patch("requests.get")
    @patch("os.getenv")
    def test_converting_transaction_into_rub_rub(self, mock_getenv, mock_get):
        test_data_rub = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }
        result = converting_transaction_into_rub(test_data_rub)
        self.assertEqual(result, 31957.58)
        mock_get.assert_not_called()


    @patch("requests.get")
    @patch("os.getenv", return_value="fake_api_key")
    def test_converting_transaction_into_rub_usd(self, mock_getenv, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {"result": 56668.30}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        test_data_usd = {
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {
      "amount": "9824.07",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
  }
        result = converting_transaction_into_rub(test_data_usd)
        self.assertEqual(result, 56668.30)


    @patch("requests.get")
    @patch("os.getenv", return_value="fake_api_key")
    def test_converting_transaction_into_rub_error(self, mock_getenv, mock_get):
        mock_get.side_effect = KeyError("API error")
        transaction = {
    "id": 522357576,
    "state": "EXECUTED",
    "date": "2019-07-12T20:41:47.882230",
    "operationAmount": {
      "amount": "51463.70",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 48894435694657014368",
    "to": "Счет 38976430693692818358"
  }
        result = converting_transaction_into_rub(transaction)
        self.assertEqual(result, [])


    @patch("requests.get")
    @patch("os.getenv", return_value="fake_api_key")
    def test_converting_transaction_into_rub_error2(self, mock_getenv, mock_get):
        mock_get.side_effect = RequestException("API error")
        transaction = {
    "id": 522357576,
    "state": "EXECUTED",
    "date": "2019-07-12T20:41:47.882230",
    "operationAmount": {
      "amount": "51463.70",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 48894435694657014368",
    "to": "Счет 38976430693692818358"
  }
        result = converting_transaction_into_rub(transaction)
        self.assertEqual(result, [])
