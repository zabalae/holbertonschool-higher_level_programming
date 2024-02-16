#!/usr/bin/python3
'''Class Base'''


import json


class Base:
    '''Class Base'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Initialization of Base'''

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ 
        returns JSON representation of list_dictionaries 
        """
        if list_dictionaries is None or list_dictionaries == []:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
        """
        objs = []
        if list_objs is not None:
            for x in list_objs:
                objs.append(cls.to_dictionary(x))
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(cls.to_json_string(objs))
