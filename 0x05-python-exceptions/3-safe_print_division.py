#!/usr/bin/python3
def safe_print_division(a, b):
    c = None
    try:
        c = a / b
        return c
    except (ZeroDivisionError, ValueError, TypeError):
        return c
    finally:
        print("Inside result: {}".format(c))
