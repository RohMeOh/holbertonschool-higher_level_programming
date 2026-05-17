#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function."""

    def test_ordered_list(self):
        """Test ordered list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test unordered list."""
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_single_element(self):
        """Test list with one element."""
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        """Test list with negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test list with positive and negative numbers."""
        self.assertEqual(max_integer([-5, 10, 3, -1]), 10)

    def test_float_numbers(self):
        """Test list with float numbers."""
        self.assertEqual(max_integer([1.1, 2.2, 3.3]), 3.3)

    def test_empty_list(self):
        """Test empty list."""
        self.assertIsNone(max_integer([]))

    def test_string_list(self):
        """Test list of strings."""
        self.assertEqual(max_integer(["a", "b", "c"]), "c")

    def test_max_at_beginning(self):
        """Test max integer at beginning."""
        self.assertEqual(max_integer([9, 3, 5, 1]), 9)

    def test_max_at_end(self):
        """Test max integer at end."""
        self.assertEqual(max_integer([1, 3, 5, 9]), 9)


if __name__ == "__main__":
    unittest.main()
