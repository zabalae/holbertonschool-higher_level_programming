#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for x in range(len(my_list)):
        if my_list[x] == search:
            my_list[x] == replace
    return my_list
