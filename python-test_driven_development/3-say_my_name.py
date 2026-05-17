#!/usr/bin/python3
"""This module defines a name printing function.

The function prints a formatted full name.
"""


def say_my_name(first_name, last_name=""):
    """Print a person's full name."""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
