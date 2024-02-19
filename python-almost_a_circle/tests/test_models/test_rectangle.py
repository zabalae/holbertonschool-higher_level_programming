#!/usr/bin/python3
'''Test Cases for rectangle class'''

#from models.base import Base
from models.rectangle import Rectangle
#import os
import unittest


class TestRectangle(unittest.TestCase):
    '''Test Cases for rectangle class'''
    def oneArgument(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

if __name__ == "__main__":
    unittest.main()
