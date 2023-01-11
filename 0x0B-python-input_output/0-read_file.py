#!/usr/bin/python3
"""A function that reads a text file"""


def read_file(filename=""):
    """A function that reads a text file
    and prints to stdout"""

    with open(filename, encoding="utf-8") as file_name:
        print(file_name.read(), end="")
