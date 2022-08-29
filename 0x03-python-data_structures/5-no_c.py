#!/usr/bin/python3
def no_c(my_string):
    newstring = ''
    for x in my_string:
        if x not in 'c' and x not in 'C':
            newstring += x
    return newstring
