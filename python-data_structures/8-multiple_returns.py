#!/usr/bin/python3
def multiple_returns(sentence):
    """Return a tuple with the length of sentence and its first char.

    If sentence is empty, the first character is None.
    """
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
