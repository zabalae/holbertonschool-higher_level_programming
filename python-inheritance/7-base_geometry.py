#!/usr/bin/python3
'''class BaseGeometry'''


class BaseGeometry:
    '''
    Class BaseGeometry
    '''

    def area(self):
        Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
