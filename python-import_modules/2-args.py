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
    index = 1
    while index < (len(sys.argv)):
        print("{:d}: {:s}".format(index, sys.argv[index]))
        index += 1
