import pytest
from pytests import __version__
from pytests.fizzbuzz import FizzBuzz, OurCustomException


@pytest.fixture
def fizz_buzz():
    return FizzBuzz()


def test_version():
    assert __version__ == '0.1.0'


def test_is_mod_three_true(fizz_buzz):
    assert fizz_buzz.is_mod_three_true(3) is True
    assert fizz_buzz.is_mod_three_true(5) is False


def test_is_mod_five_true(fizz_buzz):
    assert fizz_buzz.is_mod_five_true(3) is False
    assert fizz_buzz.is_mod_five_true(5) is True


def test_is_mod_three_and_five_true(fizz_buzz):
    assert fizz_buzz.is_mod_three_and_five_true(3) is False
    assert fizz_buzz.is_mod_three_and_five_true(5) is False
    assert fizz_buzz.is_mod_three_and_five_true(15) is True


def test_evaluate_div_by_three_is_fizz(fizz_buzz):
    assert fizz_buzz.evaluate(3) == 'Fizz'


def test_evaluate_div_by_four_is_not_fizz(fizz_buzz):
    assert fizz_buzz.evaluate(4) == 4


def test_evaluate_div_by_five_is_buzz(fizz_buzz):
    assert fizz_buzz.evaluate(5) == 'Buzz'


def test_evaluate_div_by_three_and_five_is_fizzbuzz(fizz_buzz):
    assert fizz_buzz.evaluate(15) == 'FizzBuzz'


def test_evaluate_div_by_three_and_five_is_fizzbuzz(fizz_buzz):
    with pytest.raises(OurCustomException):
        fizz_buzz.evaluate('a')
