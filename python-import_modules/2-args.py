#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv - 1) == 0 or len(sys.argv - 1) > 1:
        if len(sys.argv -1) == 0:
            print("{} arguments.".format(len(sys, argv) - 1))
        else:
            print("{} arguments:".format(len(sys, argv) - 1))
    else:
        print("{} argumnent:".format(len(sys, argv) - 1))
    for x, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(x, arg))
