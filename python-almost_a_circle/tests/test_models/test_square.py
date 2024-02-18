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

    @staticmethod
    def capture_stdout(sq, method):
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(sq)
        else:
            sq.display()
        sys.stdout = sys.__stdout__
        return capture

    def strPrintSize(self):
        s = Square(4)
        capture = TestSquare.capture_stdout(s, "print")
        correct = "[Square] ({}) 0/0 - 4\n".format(s.id)
        self.assertEqual(correct, capture.getvalue())

    def displaySize(self):
        s = Square(2, 0, 0, 9)
        capture = TestSquare.capture_stdout(s, "display")
        self.assertEqual(" ###\n##\n", capture.getvalue())

    def updateArguments(self):
        s = Square(10, 10, 10, 10)
        s.update()
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))
