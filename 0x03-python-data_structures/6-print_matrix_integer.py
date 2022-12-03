#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list_ in matrix:
        for element in list_:
            if element != list_[-1]:
                print("{}".format(element), end=" ")
            else:
                print("{}".format(element), end="")
        print()

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
