#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define a class for testing max_integer function"""

    def test_regular_list(self):
        """Test for a regular list"""
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_unordered_list(self):
        """Test for an unordered list"""
        result = max_integer([1, 3, 4, 2])
        self.assertEqual(result, 4)

    def test_empty_list(self):
        """Test for an empty list"""
        result = max_integer([])
        self.assertIsNone(result)

    def test_negative_numbers(self):
        """Test for a list containing negative numbers"""
        result = max_integer([-5, -2, -8, -1])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        """Test for a list containing mixed positive and negative numbers"""
        result = max_integer([-5, 10, -8, 3])
        self.assertEqual(result, 10)

if __name__ == '__main__':
    unittest.main()
