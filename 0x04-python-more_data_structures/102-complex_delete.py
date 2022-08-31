#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new = list(a_dictionary.keys())
    {a_dictionary.pop(key) for key in new if a_dictionary[key] == value}
    return (a_dictionary)
