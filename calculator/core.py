"""
Core calculator functions supporting add, subtract, multiply, and divide.
All functions accept and return float values to support decimals, large numbers,
negative numbers, and infinity.
"""

import math


def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of a minus b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def divide(a: float, b: float) -> float:
    """
    Return the quotient of a divided by b.

    Raises:
        ValueError: If b is zero (division by zero is undefined).

    Supports decimal divisors, negative numbers, large numbers, and infinity.
    When a is finite and b is infinity, the result is 0.0 (per IEEE 754).
    """
    # Guard against division by zero explicitly to provide a clear error message
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b
