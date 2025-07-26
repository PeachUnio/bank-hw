import json
import unittest
from json import JSONDecodeError
from unittest.mock import Mock, mock_open, patch

from src.utils import load_transactions


class TestLoadTransactions(unittest.TestCase):

    def test_load_transactions(self):
        test_data = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]

        with patch("builtins.open", mock_open(read_data=json.dumps(test_data))) as mock_file:
            with patch("json.loads", return_value=test_data):
                result = load_transactions("dummy_path.json")

                self.assertEqual(result, test_data)
                mock_file.assert_called_once_with("dummy_path.json", "r", encoding="utf-8")

    def test_load_transactions_empty_list(self):
        with patch("builtins.open", mock_open(read_data="")):
            result = load_transactions("empty.json")
            self.assertEqual(result, [])

        with patch("builtins.open", mock_open(read_data="{jison")):
            result = load_transactions("invalid.json")
            self.assertEqual(result, [])

        with patch("builtins.open", mock_open(read_data=json.dumps({"id": 1, "amount": 100}))):
            result = load_transactions("not_list.json")
            self.assertEqual(result, [])

        with patch("builtins.open", side_effect=FileNotFoundError):
            result = load_transactions("not_exist.json")
            self.assertEqual(result, [])

        with patch("builtins.open", side_effect=JSONDecodeError):
            result = load_transactions("not_exist.json")
            self.assertEqual(result, [])