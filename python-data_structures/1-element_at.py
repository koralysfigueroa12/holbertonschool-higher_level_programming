#!/usr/bin/python3
def element_at(my_list, idx):
    """Return the element at index idx of my_list.

    If idx is negative or out of range, return None.
    """
    if idx < 0:
        return None
    if idx >= len(my_list):
        return None
    return my_list[idx]
