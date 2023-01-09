#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """Class that inherits
    a list's charateristics"""

    def print_sorted(self):
        """Print a list in sorted ascending order."""

        print(sorted(self))
