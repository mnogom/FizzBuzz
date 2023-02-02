"""Unit-tests for core."""

from fizz_buzz.core import convert_number


def test_convert_number():
    assert convert_number(9) == "Fizz!"
    assert convert_number(5) == "Buzz!"
    assert convert_number(15) == "FizzBuzz!"
    assert convert_number(7) == "7"
    assert convert_number(133) == "133"

    assert convert_number(-9) == "Fizz!"
    assert convert_number(-5) == "Buzz!"
    assert convert_number(-15) == "FizzBuzz!"
    assert convert_number(-7) == "-7"
    assert convert_number(-133) == "-133"

    assert convert_number(0) == "0"
