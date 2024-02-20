#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    cpy_dict = a_dictionary.copy()
    list_keys = list(cpy_dict.keys())
    for i in list_keys:
        cpy_dict[i] *= 2
    return cpy_dict
