import pytest
from main import roman_int, int_roman, expression  # Adjust import to point to src.main

# Unit test for roman_int function
def test_roman_int():
    assert roman_int('I') == 1
    assert roman_int('IV') == 4
    assert roman_int('IX') == 9
    assert roman_int('X') == 10
    assert roman_int('XX') == 20
    assert roman_int('XL') == 40
    assert roman_int('L') == 50
    assert roman_int('XC') == 90
    assert roman_int('C') == 100
    assert roman_int('D') == 500
    assert roman_int('M') == 1000
    assert roman_int('MMMCMXCIX') == 3999

# Unit test for int_roman function
def test_int_to_roman():
    assert int_roman(1) == 'I'
    assert int_roman(4) == 'IV'
    assert int_roman(9) == 'IX'
    assert int_roman(10) == 'X'
    assert int_roman(20) == 'XX'
    assert int_roman(40) == 'XL'
    assert int_roman(50) == 'L'
    assert int_roman(90) == 'XC'
    assert int_roman(100) == 'C'
    assert int_roman(500) == 'D'
    assert int_roman(1000) == 'M'
    assert int_roman(3999) == 'MMMCMXCIX'

# Unit test for expression function
def test_expression():
    assert expression("XX + V") == 'XXV'
    assert expression("XL * II") == 'LXXX'
    assert expression("XX / II") == 'X'
    assert expression("C - L") == 'L'
    assert expression("(X + X) * II") == 'XL'

    # Invalid expression
    assert "Error" in expression("X + Invalid")

