#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    sum_products = 0
    sum_weight = 0

    for score, weight in my_list:
        sum_products += score * weight
        sum_weights += weight

    weighted_avg = sum_products / sum_weights

    return weighted_avg
