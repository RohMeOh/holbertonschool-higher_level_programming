#!/usr/bin/python3
"""This module defines an integer addition function.

The function accepts integers and floats.
Floats are converted to integers before addition.
"""


def add_integer(a, b=98):
    """Return the addition of two integers.

    Raises TypeError if a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
