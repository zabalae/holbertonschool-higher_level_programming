#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv) - 1
    if args == 0 or args > 1:
        if args == 0:
            print("{} arguments.".format(args))
        else:
            print("{} arguments:".format(args))
    else:
        print("{} argumnent:".format(args))
    for x, arg in enumerate(sys.argv[1:], start=1):
        print("{:d}: {:s}".format(x, arg))
