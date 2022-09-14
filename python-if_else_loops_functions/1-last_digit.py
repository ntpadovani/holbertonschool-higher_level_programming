#!/usr/bin/python3
import random
from re import I
number = random.randint(-10000, 10000)
if number > 10:
    intero = number % 10
elif number < -10:
    intero = -number % 10
    intero = -intero
else:
    intero = number

if intero > 5:
    print(f"Last digit of {number} is {intero} and is greater than 5")
elif intero == 0:
    print(f"Last digit of {number} is {intero} and is 0")
else:
    print(f"Last digit of {number} is {intero} and is less than 6 and not 0")
