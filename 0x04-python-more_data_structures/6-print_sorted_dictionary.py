#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
        # iterate thriugh the key-value pair in the dictionary
        for key, value in sorted(a_dictionary.items()):
                # print each pair
                print("{}: {}".format(key, value))