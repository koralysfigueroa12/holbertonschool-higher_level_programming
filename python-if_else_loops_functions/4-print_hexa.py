#!/usr/bin/python3
"""Print numbers from 0 to 98 in decimal and hexadecimal.

Constraints:
- only one print with string format
- only one loop
- do not store numbers/strings in variables
- do not import any module
"""

for i in range(99):
    print("{} = 0x{:x}".format(i, i))
