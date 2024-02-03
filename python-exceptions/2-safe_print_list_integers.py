#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    ints_printed = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ints_printed += 1
        except (TypeError, ValueError):
            pass
        print()
        return ints_printed
