#!/usr/bin/python3
"""A function that returns the list of available
attributes and methods of an object
"""


def lookup(obj):
    """Returns lists containing
    methods and attributes of an object"""

    return (dir(obj))
