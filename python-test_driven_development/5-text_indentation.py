#!/usr/bin/python3
"""This module defines a text indentation function.

The function prints text with two new lines after
'.', '?' and ':' characters.
"""


def text_indentation(text):
    """Print text with two new lines after special characters."""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0

    while i < len(text):
        print(text[i], end="")

        if text[i] in ".?:":
            print("\n")

            i += 1

            while i < len(text) and text[i] == " ":
                i += 1

            continue

        i += 1
