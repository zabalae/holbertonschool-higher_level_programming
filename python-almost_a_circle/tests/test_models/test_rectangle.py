#!/usr/bin/python3
'''Test Cases for rectangle class'''

from models.base import Base
from models.rectangle import Rectangle
#import os
import json
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

    def saveToFileNone(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            content = json.load(f)
            self.assertEqual(content, [])

    def testUpdateDict(self):
        r1 = Rectangle(1, 3)
        r1.update(id=3, height=5, width=6, x=7, y=9)
        self.assertEqual(6, r1.width)

if __name__ == "__main__":
    unittest.main()
