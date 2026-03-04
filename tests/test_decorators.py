import os

import pytest

from src.decorators.log import log


def test_log_to_console_success(capsys):
    @log()
    def add(a, b):
        return a + b

    result = add(1, 2)
    captured = capsys.readouterr()

    assert result == 3
    assert "add ok" in captured.out


def test_log_to_console_error(capsys):
    @log()
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    captured = capsys.readouterr()
    assert "divide error" in captured.out
    assert "Inputs:" in captured.out


def test_log_to_file_success(tmp_path):
    log_file = tmp_path / "log.txt"

    @log(filename=str(log_file))
    def multiply(a, b):
        return a * b

    result = multiply(2, 3)

    assert result == 6
    content = log_file.read_text(encoding="utf-8")
    assert "multiply ok" in content


def test_log_to_file_error(tmp_path):
    log_file = tmp_path / "log.txt"

    @log(filename=str(log_file))
    def fail():
        raise ValueError("fail")

    with pytest.raises(ValueError):
        fail()

    content = log_file.read_text(encoding="utf-8")
    assert "fail error" in content
    assert "Inputs:" in content
