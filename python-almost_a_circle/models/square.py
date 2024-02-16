#!/usr/bin/python3
'''Square class'''


from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square class'''
    def __init__(self, size, x=0, y=0, id=None):
        '''Initialize a square'''
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """get size"""
        return (self.width)

    @size.setter
    def size(self, value):
        """set size"""
        self.width = value
        self.height = value

    def __str__(self):
        """
        __str__ method
        """
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__, self.id, self.x, self.y,
            self.size)

    def update(self, *args, **kwargs):
        """
        method that assigns attributes
        """
        if args:
            for k, v in enumerate(args):
                if k == 0:
                    self.id = v
                elif k == 1:
                    self.size = v
                elif k == 2:
                    self.x = v
                else:
                    self.y = v
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
