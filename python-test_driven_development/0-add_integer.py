#!/usr/bin/python3
"""
This module provides integer addition.

Inputs may be integers or floats.
"""


def add_integer(a, b=98):
    """Add two values after validating their types.
    Return the sum as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
