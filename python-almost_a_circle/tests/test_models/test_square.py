#!/usr/bin/python3
'''Test cases for square class'''


import unittest
import io
from models.base import Base
from models.square import Square
import sys


class TestSquare(unittest.TestCase):
    '''Test Cases for square class'''
    def neArgument(self):
        s1 = Square(10)
        s2 = Square(11)
        self.assertEqual(s1.id, s2.id - 1)

    def twoArguments(self):
        s1 = Square(10, 2)
        s2 = Square(2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def sizeGetter(self):
        self.assertEqual(5, Square(5, 2, 3, 9).size)

    def widthGetter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.width)

    def heightGetter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.height)

if __name__ == "__main__":
    unittest.main()
