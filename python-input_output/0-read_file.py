#!/usr/bin/python3
'''Function that reads a text file (UTF8) and prints it to stdout'''


def read_file(filename=""):
    '''read_file function'''
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
