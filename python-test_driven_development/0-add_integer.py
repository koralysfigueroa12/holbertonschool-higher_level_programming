#!/usr/bin/python3
"""0-add_integer module.

This module provides a function that adds two integers.
"""


def add_integer(a, b=98):
    """Return the addition of a and b as integers.

    a and b must be integers or floats; floats are casted to
    integers before the addition.

    Raises:
        TypeError: if a or b are not an integer or float. The message
        must be exactly "a must be an integer" or "b must be an integer".

    Returns:
        int: the sum of a and b after casting to int if needed.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
