#!/usr/bin/python3
'''Test Cases for rectangle class'''

#from models.base import Base
from models.rectangle import Rectangle
#import os
import unittest


class TestRectangle(unittest.TestCase):
    '''Test Cases for rectangle class'''
    def test_zero_height(self):
        """Tests whn the height is zero"""
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
