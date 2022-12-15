#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    # Create a list of keys to delete
    keys_to_delete = []

    # Iterate over the a_dictionary and add the keys whose value is equal to the specified value to the list of keys to delete
    for key, val in a_dictionary.items():
        if val == value:
            keys_to_delete.append(key)

    # Iterate over the list of keys to delete and remove them from the a_dictionary
    for key in keys_to_delete:
        del a_dictionary[key]

    # Return the modified a_dictionary
    return a_dictionary
