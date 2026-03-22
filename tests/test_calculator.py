"""
Unit tests for the calculator package.
Uses pytest. Covers all edge cases including decimals, negatives,
large numbers, infinity, and divide-by-zero.
"""

import math
import pytest
from calculator import add, subtract, multiply, divide


# ---------------------------------------------------------------------------
# add
# ---------------------------------------------------------------------------

def test_add_positive_integers():
    # Basic addition of two positive integers
    assert add(3, 4) == 7


def test_add_negative_numbers():
    # Adding two negative numbers should give a more negative result
    assert add(-3, -4) == -7


def test_add_mixed_sign():
    # Positive + negative
    assert add(10, -3) == 7


def test_add_zero():
    # Adding zero should return the other operand unchanged
    assert add(5, 0) == 5


def test_add_decimals():
    # Floating-point addition
    assert add(0.1, 0.2) == pytest.approx(0.3)


def test_add_large_numbers():
    # Numbers well beyond typical 32-bit integer range
    assert add(10**18, 10**18) == 2 * 10**18


def test_add_infinity():
    # inf + finite == inf
    assert add(math.inf, 1) == math.inf


def test_add_negative_infinity():
    # -inf + finite == -inf
    assert add(-math.inf, 1) == -math.inf


def test_add_both_infinity():
    # inf + inf == inf
    assert add(math.inf, math.inf) == math.inf


# ---------------------------------------------------------------------------
# subtract
# ---------------------------------------------------------------------------

def test_subtract_positive_integers():
    assert subtract(10, 3) == 7


def test_subtract_negative_numbers():
    # Subtracting a negative is equivalent to adding its absolute value
    assert subtract(-5, -3) == -2


def test_subtract_mixed_sign():
    assert subtract(5, -3) == 8


def test_subtract_zero():
    assert subtract(7, 0) == 7


def test_subtract_decimals():
    assert subtract(1.5, 0.5) == pytest.approx(1.0)


def test_subtract_large_numbers():
    assert subtract(10**18, 10**18) == 0


def test_subtract_infinity():
    # inf - finite == inf
    assert subtract(math.inf, 100) == math.inf


def test_subtract_same_infinity():
    # inf - inf is NaN (undefined)
    result = subtract(math.inf, math.inf)
    assert math.isnan(result)


# ---------------------------------------------------------------------------
# multiply
# ---------------------------------------------------------------------------

def test_multiply_positive_integers():
    assert multiply(3, 4) == 12


def test_multiply_negative_numbers():
    # Negative * Negative == Positive
    assert multiply(-3, -4) == 12


def test_multiply_mixed_sign():
    # Positive * Negative == Negative
    assert multiply(3, -4) == -12


def test_multiply_by_zero():
    assert multiply(1000, 0) == 0


def test_multiply_decimals():
    assert multiply(0.5, 0.4) == pytest.approx(0.2)


def test_multiply_large_numbers():
    assert multiply(10**9, 10**9) == 10**18


def test_multiply_infinity():
    # Any non-zero finite * inf == inf
    assert multiply(2, math.inf) == math.inf


def test_multiply_negative_infinity():
    # Negative finite * inf == -inf
    assert multiply(-2, math.inf) == -math.inf


def test_multiply_zero_by_infinity():
    # 0 * inf is NaN per IEEE 754
    result = multiply(0, math.inf)
    assert math.isnan(result)


# ---------------------------------------------------------------------------
# divide
# ---------------------------------------------------------------------------

def test_divide_positive_integers():
    assert divide(10, 2) == 5.0


def test_divide_negative_dividend():
    assert divide(-10, 2) == -5.0


def test_divide_negative_divisor():
    assert divide(10, -2) == -5.0


def test_divide_both_negative():
    # Negative / Negative == Positive
    assert divide(-10, -2) == 5.0


def test_divide_decimals():
    # Division with decimal divisor
    assert divide(1, 0.5) == pytest.approx(2.0)


def test_divide_decimal_result():
    # Result is a non-integer decimal
    assert divide(1, 3) == pytest.approx(1 / 3)


def test_divide_large_numbers():
    assert divide(10**18, 10**9) == pytest.approx(10**9)


def test_divide_by_zero_raises():
    # Dividing by zero must raise ValueError
    with pytest.raises(ValueError, match="Division by zero"):
        divide(5, 0)


def test_divide_zero_by_zero_raises():
    # 0/0 is also undefined and must raise ValueError
    with pytest.raises(ValueError, match="Division by zero"):
        divide(0, 0)


def test_divide_infinity_by_finite():
    # inf / finite == inf
    assert divide(math.inf, 2) == math.inf


def test_divide_finite_by_infinity():
    # Any finite number / inf == 0
    assert divide(5, math.inf) == 0.0


def test_divide_infinity_by_infinity():
    # inf / inf is NaN per IEEE 754
    result = divide(math.inf, math.inf)
    assert math.isnan(result)


def test_divide_negative_infinity():
    # -inf / positive == -inf
    assert divide(-math.inf, 2) == -math.inf
