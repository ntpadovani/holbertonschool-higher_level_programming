#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argu = len(sys.argv)
    if argu == 1:
        print("{} arguments.".format(argu - 1))
    elif argu == 2:
        print("{} argument:".format(argu - 1))
    else:
        print("{} arguments:".format(argu - 1))

    for i in range(1, argu):
        print("{}: {}".format(i, sys.argv[i]))
