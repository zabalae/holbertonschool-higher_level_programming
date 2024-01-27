#!/usr/bin/python3
def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
def uppercase(str):
    for ch in str:
        if islower(ch):
            ch = "{:c}".format(ord(ch) - 32)
        print(ch, end="")
    print("")

