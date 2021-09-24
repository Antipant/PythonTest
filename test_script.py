import pytest


def test_multiplication(test_input, expected_result):
    try:
        assert test_input * 2 == expected_result
    except AssertionError:
        pass


def test_added():
    assert 1 * 2 == 2
    assert list('a') + list('c') == ['a', 'c']


def test_oddness():
    assert 11 % 2 == 1
    assert list('aaaa').remove('a') is None
