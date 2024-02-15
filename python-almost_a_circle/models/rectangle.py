#!/usr/bin/python3
'''rectangle class'''


from models.base import Base


class Rectangle(Base):
    '''Rectangle class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        '''get width'''
        return (self.__width)

    @width.setter
    def width(self, value):
        '''set width'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''get height'''
        return (self.__height)

    @height.setter
    def height(self, value):
        '''set height'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''get x'''
        return (self.__x)

    @x.setter
    def y(self, value):
        '''set x'''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''get y'''
        return (self.__y)

    @y.setter
    def y(self, value):
        '''set y'''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''calculate the area'''
        return (self.width * self.height)

    def display(self):
        '''method that prints in stdout'''
        if self.width == 0 or self.height == 0:
            print("")
            return
        for h in range(self.height):
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        '''Return a string representation of rectangle'''
        s = "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
        return s
