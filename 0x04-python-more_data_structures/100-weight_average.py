#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    sum_of_products = 0
    sum_of_weights = 0

    for tuple_ in my_list:
        sum_of_products += tuple_[0] * tuple_[1]
        sum_of_weights += tuple_[1]

    return (sum_of_products / sum_of_weights)
