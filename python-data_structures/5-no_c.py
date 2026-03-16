#!/usr/bin/python3
def no_c(my_string):
    """Return a copy of my_string with all 'c' and 'C' removed.

    Does not use str.replace().
    """
    return ''.join(ch for ch in my_string if ch != 'c' and ch != 'C')
