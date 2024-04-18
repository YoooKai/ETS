import pytest

from functions import a_greater_than, is_pangram, sum_nums


def test_sum_nums():
    assert sum_nums(2, 2) == 4


def test_a_greater_than():
    assert a_greater_than(10, 2)


def test_is_pangram():
    assert not is_pangram('la rata pepi se come zanahoria y un aguacate')


@pytest.mark.parametrize('input_x, input_y, expected', [(5, 1, 6), (6, sum_nums(4, 2), 12)])
def test_sum_nums_params(input_x, input_y, expected):
    assert sum_nums(input_x, input_y) == expected


@pytest.mark.parametrize('text, expected', [('Jackdaws love my big sphinx of quartz', True)])
def test_is_pangram_params(text, expected):
    assert is_pangram(text) == expected
