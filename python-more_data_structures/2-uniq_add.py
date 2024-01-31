#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = 0
    for x in set(my_list):
        uniq += x
    return uniq
