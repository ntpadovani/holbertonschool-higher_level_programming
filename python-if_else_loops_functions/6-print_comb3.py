#!/usr/bin/python3
for a in range(10):
    for b in range(10):
        if a * 10 + b < b * 10 + a:
            print("{}{}".format(a, b), end="")
            if a * 10 + b < 89:
                print(end=", ")
print()