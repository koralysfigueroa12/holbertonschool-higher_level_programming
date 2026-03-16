#!/usr/bin/python3
"""Print the last digit of a randomly generated number with a message.

The variable `number` must not be changed (set by random.randint).
"""
import random

number = random.randint(-10000, 10000)

# compute last digit keeping sign for negative numbers
last = abs(number) % 10
if number < 0:
    last = -last

if last > 5:
    msg = "and is greater than 5"
elif last == 0:
    msg = "and is 0"
else:
    msg = "and is less than 6 and not 0"

print(f"Last digit of {number} is {last} {msg}")
