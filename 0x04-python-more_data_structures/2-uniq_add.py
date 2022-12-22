#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Create a set to store the unique integers
    unique_integers = set()
    
    # Iterate over the list
    for i in my_list:
        # Check if the current element is an integer 
        # and add it to the set
        # if it is not already in the set
        if isinstance(i, int) and i not in unique_integers:
            unique_integers.add(i)
    
    # Return the sum of the elements in the set
    return sum(unique_integers)
