#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replace element at idx of my_list with element.

    If idx is negative or out of range, do nothing and return
    the original list.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
