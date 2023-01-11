#!/usr/bin/python3
"""Returns dictionary description for json
serialization"""


def class_to_json(obj):
    """Function returns dictionary descrition with simple
    data structure for JSON serialisation of object

    Args:
        obj: instance of a class"""

    return obj.__dict__
