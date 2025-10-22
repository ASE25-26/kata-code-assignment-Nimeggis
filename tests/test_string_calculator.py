import pytest
from src.string_calculator import add

def test_empty_string_returns_zero():
    assert add("") == 0

def test_single_number_returns_value():
    assert add("5") == 5

def test_two_numbers_comma_separated():
    assert add("1,2") == 3

def test_multiple_numbers_comma_separated():
    assert add("1,2,3,4") == 10

def test_newlines_as_delimiters():
    assert add("1\n2,3") == 6

def test_custom_delimiter():
    assert add("//;\n1;2") == 3

def test_negative_numbers_throw():
    with pytest.raises(ValueError) as excinfo:
        add("1,-2,3,-4")
    msg = str(excinfo.value)
    assert "-2" in msg and "-4" in msg

def test_ignore_numbers_greater_than_1000():
    assert add("2,1001") == 2
    assert add("2,1000") == 1002

def test_long_delimiter_syntax():
    assert add("//[***]\n1***2***3") == 6

def test_multiple_delimiters():
    assert add("//[*][%]\n1*2%3") == 6
    assert add("//[***][%%]\n1***2%%3") == 6