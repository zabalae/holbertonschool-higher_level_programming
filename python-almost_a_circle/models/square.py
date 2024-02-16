#!/usr/bin/python3
'''Square class'''


from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square class'''
    def __init__(self, size, x=0, y=0, id=None):
        '''Initialize a square'''
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
        __str__ method
        """
        return ("[Square] ({}) {}/{} - {}".format
                (self.id, self.x, self.y, self.size))
