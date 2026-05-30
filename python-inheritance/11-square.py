#!/usr/bin/python3
"""Module containing Square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Initialize square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return square description"""
        return "[Square] {}/{}".format(self.__size, self.__size)
