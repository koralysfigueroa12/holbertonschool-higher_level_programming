#!/usr/bin/python3
"""Print the ASCII alphabet in lowercase excluding 'q' and 'e', no newline.

Constraints:
- only one print with string format
- only one loop
- do not store characters in a variable
- do not import any module
"""

print("{}".format(''.join(chr(i) for i
in range(97, 123) if i not in (101, 113))), end="")
