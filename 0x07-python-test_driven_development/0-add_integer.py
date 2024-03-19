#!/usr/bin/python3
""" A function Add"""


def add_integer(a, b=98):

    """ An add function """
    if not a or not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not b or not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
