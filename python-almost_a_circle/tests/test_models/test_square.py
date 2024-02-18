#!/usr/bin/python3
'''Test cases for square class'''


import unittest
import io
from models.base import Base
from models.square import Square
import sys


class TestSquare(unittest.TestCase):
    '''Tests for square.py'''
    def setUp(self) -> None:
        '''setUp'''
        return super().setUp()

    def tearDown(self) -> None:
        '''tearDown'''
        return super().tearDown()

    def testArea(self):
        '''Test area'''
        square1 = Square(40)
        self.assertEqual(square1.area(), 40 * 40)

    def oneArgument(self):
        square1 = Square(15)
        square2 = Square(16)
        self.assertEqual(square1.id, square2.id -1)

    def twoArguments(self):
        square1 = Square(10, 5)
        square2 = Square(5, 10)
        self.assertEqual(square1.id, square2.id -1)

