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

    def SaveToFileNoargs(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def aveToFileType(self):
        Rectangle.save_to_file([Rectangle(1, 2, 3, 4, 5)])
        with open("Rectangle.json", "r") as f:
            content = f.read()
            self.assertEqual(str, type(content))

if __name__ == "__main__":
    unittest.main()
