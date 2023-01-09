#!/usr/bin/python3
is_same_class = __import__('2-is_same_class').is_same_class

for a in [1, 1.0, "one"]:
    if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, int.__name__))
    if is_same_class(a, float):
        print("{} is an instance of the class {}".format(a, float.__name__))
    if is_same_class(a, str):
        print("{} is an instance of the class {}".format(a, object.__name__))
