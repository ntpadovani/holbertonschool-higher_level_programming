#!/usr/bin/python3
def pow(a, b):
    r = a
    n = b * -1
    if b == 0:
        return 1
    if b == 1:
        return a
    if b < 0:
        if b == -2:
            r = r * a
            return 1 / r
        for i in range(n - 1):
            r = r * a
        r = 1 / r
    for i in range(b - 1):
        r = r * a
    return r
