#!/usr/bin/python3
'''Class square that inherits from Rectangle(9-rectangle.py)'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Class square'''
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
