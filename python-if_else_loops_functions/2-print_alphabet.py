#!/usr/bin/python3
"""Print the ASCII alphabet in lowercase without a trailing newline.

Constraints:
- use only one print function with string format
- use only one loop
- do not store characters in a variable
- do not import any module
"""

print("{}".format(''.join(chr(i) for i in range(97, 123))), end="")
