#!/usr/bin/python3
'''Test cases for class Base'''


import unittest
import json
import pep8
import os
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestPep8(unittest.TestCase):
    '''Test pep8'''
    def case_pep8(self):
        '''Tests pep8'''
        stylepep8 = pep8.StyleGuide(quiet=True)
        files = ["models/base.py", "tests/test_base.py"]
        results = stylepep8.check_files(files)
        self.assertEqual(results.total_errors, 0, "Fix pep8")

class TestBase(unittest.TestCase):
    '''Tests for base.py'''
    def setUp(self) -> None:
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_id_auto(self):
        '''Tests the assigment of id automatically'''
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(15)
        b5 = Base()
        self.assertTrue(b1, self.id == 1)
        self.assertTrue(b2, self.id == 2)
        self.assertTrue(b3, self.id == 3)
        self.assertTrue(b4, self.id == 15)
        self.assertTrue(b5, self.id == 4)

    def test_id_given(self):
        """Tests the matching of id given"""
        self.assertTrue(Base(200), self.id == 200)
        self.assertTrue(Base(-5), self.id == -5)
        self.assertTrue(Base(91432), self.id == 91432)
        self.assertTrue(Base(0), self.id == 0)

    def test_id_is_none(self):
        """Test id is none
        """
        self.assertTrue(Base(), self.id == 1)
        self.assertTrue(Base(), self.id == 2)
        self.assertTrue(Base(), self.id == 3)

    def test_1_id(self):
        """After run set of ids"""
        Base._Base__nb_objects = 0
        bas = Base()
        self.assertEqual(bas.id, 1)
        t1 = Base(25)
        self.assertEqual(t1.id, 25)
        t2 = Base(-45)
        self.assertEqual(t2.id, -45)
        t3 = Base()
        self.assertEqual(t3.id, 2)

    def test_private_att_access(self):
        """Tests access of private attribute"""
        with self.assertRaises(AttributeError):
            Base.__nb_objects
            Base.nb_objects
            Base._nb_objects

    def test_invalid_args(self):
        """Tests more than one args given"""
        with self.assertRaises(TypeError):
            Base(55, 15)

    def test_attribute_error(self):
        """Tests when accessing prvate class attr"""
        b = Base(67)
        with self.assertRaises(AttributeError):
            print(b.nb_objects)
        with self.assertRaises(AttributeError):
            print(b.__nb_objects)
