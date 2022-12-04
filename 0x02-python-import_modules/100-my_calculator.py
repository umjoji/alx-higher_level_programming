#!/usr/bin/python3
# Author: George Akanimoh

if __name__ == "__main__":
    """Handle basic arithmetic operations"""
    from calculator_1 import add, sub, mul, div
    import sys

    # if command line args not 3 print error msg
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # create a dictionary to store operators
    # and function names
    operators = {"+": add, "-": sub, "*": mul, "/": div}

    # print error msg if operator not in dict keys
    if sys.argv[2] not in list(operators.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # cast command line args to int
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    # print formatted output
    x = sys.argv[2]
    print("{} {} {} = {}".format(a, x, b, operators[x](a, b)))
