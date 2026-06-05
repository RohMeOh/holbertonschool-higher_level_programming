#!/usr/bin/python3
"""Student class module."""


class Student:
    """Defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the instance."""
        if type(attrs) is list:
            new_dict = {}

            for attr in attrs:
                if type(attr) is str and attr in self.__dict__:
                    new_dict[attr] = self.__dict__[attr]

            return new_dict

        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the instance."""
        for key, value in json.items():
            setattr(self, key, value)
