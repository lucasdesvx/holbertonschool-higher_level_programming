#!/usr/bin/python3
"""Unittests for max_integer."""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for finding the maximum integer in a list."""

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_default_empty_list(self):
        self.assertIsNone(max_integer())

    def test_one_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_increasing_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_decreasing_list(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_values(self):
        self.assertEqual(max_integer([-4, -1, -8, -3]), -1)

    def test_repeated_maximum(self):
        self.assertEqual(max_integer([5, 1, 5, 2]), 5)


if __name__ == "__main__":
    unittest.main()
