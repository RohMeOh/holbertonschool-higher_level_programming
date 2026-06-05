#!/usr/bin/python3
"""Module that creates an object from a JSON string."""

import json


def from_json_string(my_str):
    """Return the Python object represented by a JSON string."""
    return json.loads(my_str)
