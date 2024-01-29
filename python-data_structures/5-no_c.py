#!/usr/bin/python3

def no_c(my_string):
    str_list = list(my_string)
    mystring = ''
    for ch in str_list:
        if ch != 'C' and ch != 'c':
            mystring += ch
    return mystring


