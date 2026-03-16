#!/usr/bin/python3
"""Print numbers from 00 to 99 separated by ", ".

Constraints:
- no more than 2 print functions with string format
- only one loop
- do not store numbers or strings in a variable
- do not import any module
"""

for i in range(100):
    if i != 99:
        print("{:02d}, ".format(i), end="")
    else:
        print("{:02d}".format(i))
