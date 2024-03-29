#!/usr/bin/python3
'''Square class'''


from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square class'''
    def __init__(self, size, x=0, y=0, id=None):
        '''Initialize a square'''
        super().__init__(width=size, height=size, x=x, y=y, id=id)

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
        value = "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                  self.y, self.width)
        return (value)

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

    def to_dictionary(self):
        """Return dictionary representation of a square"""
        dict = {}
        dict["id"] = self.id
        dict["size"] = self.size
        dict["x"] = self.x
        dict["y"] = self.y
        return dict
