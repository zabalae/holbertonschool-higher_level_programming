#!/usr/bin/python3
'''
Class MyList that inherits from list:
'''


class MyList(list):
    '''
    Public instance method that prints the list sorted
    '''
    def print_sorted(self):
        print(sorted(self))