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

    def testArea(self):
        '''Test area'''
        square1 = Square(40)
        self.assertEqual(square1.area(), 40 * 40)