import pytest
from main import roman_to_int, int_to_roman, evaluate_expression  # Adjust import to point to src.main

# Unit test for roman_to_int function
def test_roman_to_int():
    assert roman_to_int('I') == 1
    assert roman_to_int('IV') == 4
    assert roman_to_int('IX') == 9
    assert roman_to_int('X') == 10
    assert roman_to_int('XX') == 20
    assert roman_to_int('XL') == 40
    assert roman_to_int('L') == 50
    assert roman_to_int('XC') == 90
    assert roman_to_int('C') == 100
    assert roman_to_int('D') == 500
    assert roman_to_int('M') == 1000
    assert roman_to_int('MMMCMXCIX') == 3999

# Unit test for int_to_roman function
def test_int_to_roman():
    assert int_to_roman(1) == 'I'
    assert int_to_roman(4) == 'IV'
    assert int_to_roman(9) == 'IX'
    assert int_to_roman(10) == 'X'
    assert int_to_roman(20) == 'XX'
    assert int_to_roman(40) == 'XL'
    assert int_to_roman(50) == 'L'
    assert int_to_roman(90) == 'XC'
    assert int_to_roman(100) == 'C'
    assert int_to_roman(500) == 'D'
    assert int_to_roman(1000) == 'M'
    assert int_to_roman(3999) == 'MMMCMXCIX'

# Unit test for evaluate_expression function
def test_equation():
    assert evaluate_expression("XX + V") == 'XXV'
    assert evaluate_expression("XL * II") == 'LXXX'
    assert evaluate_expression("XX / II") == 'X'
    assert evaluate_expression("C - L") == 'L'
    assert evaluate_expression("(X + X) * II") == 'XL'

    # Invalid expression
    assert "Error" in evaluate_expression("X + Invalid")

