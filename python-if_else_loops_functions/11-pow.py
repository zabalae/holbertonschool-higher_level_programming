#!/usr/bin/python3
def pow(a, b):
    x = 1
    result = a
    while x <= b:
        result = result * a
        x++
    return result
