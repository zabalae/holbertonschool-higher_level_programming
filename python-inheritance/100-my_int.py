#!/usr/bin/python3
'''class MyInt that inherits from int'''


class MyInt(int):
    '''MyInt has == and != operators inverted'''
    def __init__(self, value):
        self.__value = value

    def __eq__(self, other):
        return self.__value is not other

    def __ne__(self, other):
        return self.__value is other
