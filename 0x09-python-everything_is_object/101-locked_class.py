#!/usr/bin/python3
class LockedClass:
        """
        Use the __slot__ atrribute to prevent additionof other
        instance atrributes
        """
        __slots__ = ["first_name"]
