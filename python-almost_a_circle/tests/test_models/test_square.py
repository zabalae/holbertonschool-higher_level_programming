#!/usr/bin/python3
'''Test cases for square class'''


import unittest
import io
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    '''Tests for square.py'''
    def setUp(self) -> None:
        '''setUp'''
        return super().setUp()

    def tearDown(self) -> None:
        '''tearDown'''
        return super().tearDown()

    def testForList(self):
        '''Test wrong size'''
        with self.assertRaises(TypeError):
            square1 = Square([3, 8])
            square2 = Square(3, [4, 6], 9)

    def testForStr(self):
        '''Test wrong size'''
        with self.assertRaises(TypeError):
            square1 = Square(5, "H")
            square2 = Square(6, "T", 8)

    def testForBool(self):
        '''Test Wrong size'''
        with self.assertRaises(TypeError):
            square1 = Square(False)
            square2 = Square(5, False, 7)

    def testArea(self):
        '''Test area'''
        square1 = Square(40)
        self.assertEqual(square1.area(), 40 * 40)