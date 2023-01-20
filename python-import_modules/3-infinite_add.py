#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    idx = 1
    sum = 0
    if len(argv) == 1:
        print("0")
    else:
        for i in range(len(argv) - 1):
            sum = int(argv[idx]) + sum
            idx += 1
        print("{:d}".format(sum))
