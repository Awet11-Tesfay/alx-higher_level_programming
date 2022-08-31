#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    uni_sum = set(my_list)
    for i in uni_sum:
        sum += i
    return sum
