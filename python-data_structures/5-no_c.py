#!/usr/bin/python3

def no_c(my_string):
    str_list = list(my_string)
    string = ''
    for ch in str_list:
        if ch != 'C' and ch != 'c':
            string += ch
        return string


