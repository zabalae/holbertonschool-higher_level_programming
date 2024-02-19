#!/usr/bin/python3
'''Test Cases for rectangle class'''

from models.base import Base
from models.rectangle import Rectangle
#import os
import unittest


class TestRectangle(unittest.TestCase):
    '''Test Cases for rectangle class'''
    def rectangleIsBase(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def oneArgument(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def noArguments(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

if __name__ == "__main__":
    unittest.main()
