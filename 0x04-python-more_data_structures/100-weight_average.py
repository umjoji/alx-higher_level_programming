#!/usr/bin/python3
def weight_average(my_list=[]):
    sum_of_products = 0
    sum_of_weights = 0
    for i in range(len(my_list)):
        # Get the integer and its corresponding weight
        x = my_list[i][0]
        w = my_list[i][1]

        # Multiply the integer by its weight
        product = x * w

        # Add the product to the sum of products
        sum_of_products += product

        # Add the weight to the sum of weights
        sum_of_weights += w

    # Divide the sum of products by the sum of weights to get the weighted average
    return sum_of_products / sum_of_weights
