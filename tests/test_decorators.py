from os import access

import pytest

from src.decorators import format_inputs, log


def test_log_print(capsys):
    @log()
    def add_numbers(a, b):
        return a + b

    result = add_numbers(5, 3)
    captured = capsys.readouterr()
    assert captured.out == "8\nadd_numbers ok\n"


def test_log_print_error(capsys):
    @log()
    def fail_func():
        raise ValueError("Test error")

    with pytest.raises(ValueError):
        fail_func()

    captured = capsys.readouterr()
    assert captured.out == "fail_func error: Test error Inputs: no inputs\n"


def test_log_file(tmp_path):
    filename = tmp_path / "test.txt"

    @log(filename)
    def add_numbers(a, b):
        return a + b

    result = add_numbers(5, 7)
    assert result == 12
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        assert "12\nadd_numbers ok" in content


def test_log_file_error(tmp_path):
    filename = tmp_path / "error.txt"

    @log(filename)
    def divide_numbers(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide_numbers(13, 0)

    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        assert "divide_numbers error: division by zero Inputs: args: (13, 0)" in content


def test_format_inputs():
    assert "args: (1, 2)" in format_inputs((1, 2), {})

    assert "kwargs: {'a': 1}" in format_inputs((), {"a": 1})

    assert "no inputs" == format_inputs((), {})
