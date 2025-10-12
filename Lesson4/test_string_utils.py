import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_text, expected_text",
                         [
                             ("book", "Book"),
                             ("good day", "Good day"),
                             ("ТЕСТ", "Тест"),
                         ])
def test_capitalize_positive(input_text, expected_text):
    assert string_utils.capitalize(input_text) == expected_text


@pytest.mark.parametrize("input_text, expected_text",
                         [
                             (" mop", "mop"),
                             (" Hello world", "Hello world"),
                             ("   test", "test"),
                         ])
def test_trim_positive(input_text, expected_text):
    assert string_utils.trim(input_text) == expected_text


@pytest.mark.parametrize("input_text, symbol, bool",
                         [
                             ("Test", "s", True),
                             ("Hello world", "H", True),
                             ("123", "1", True),
                         ])
def test_contains_positive(input_text, symbol, bool):
    assert string_utils.contains(input_text, symbol) == bool


@pytest.mark.parametrize("input_text, symbol, expected_text",
                         [
                             ("Test", "s", "Tet"),
                             ("Hello world", "l", "Heo word"),
                             ("Время", "м", "Врея"),
                             ("Начало дня", " ", "Началодня"),
                         ])
def test_delete_symbol_positive(input_text, symbol, expected_text):
    assert string_utils.delete_symbol(input_text, symbol) == expected_text


@pytest.mark.negative
@pytest.mark.parametrize("input_text, expected_text",
                         [
                             ("123abc", "123abc"),
                             ("", ""),
                             ("  ", "  "),
                         ])
def test_capitalize_neganive(input_text, expected_text):
    assert string_utils.capitalize(input_text) == expected_text


@pytest.mark.parametrize("input_text, expected_text",
                         [
                             ("mop", "mop"),
                             ("   ", ""),
                             ("Hello world", "Hello world"),
                         ])
def test_trim_negative(input_text, expected_text):
    assert string_utils.trim(input_text) == expected_text


@pytest.mark.parametrize("input_text, symbol, bool",
                         [
                             ("Test", "S", False),
                             ("Hello world", " ", True),
                             ("Book", "t", False),
                         ])
def test_contains_negative(input_text, symbol, bool):
    assert string_utils.contains(input_text, symbol) == bool


@pytest.mark.parametrize("input_text, symbol, expected_text",
                         [
                             ("Test", "E", "Test"),
                             ("Hello world", "h", "Hello world"),
                             ("", "j", ""),
                         ])
def test_delete_symbol_negative(input_text, symbol, expected_text):
    assert string_utils.delete_symbol(input_text, symbol) == expected_text
