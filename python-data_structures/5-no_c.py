#!/usr/bin/python3
def no_c(my_string):
    new_list = list(my_string)
    idx = 0
    while idx < len(new_list):
        if new_list[idx] == 'c' or new_list[idx] == 'C':
            new_list.pop(idx)
            idx -= 1
        idx += 1
    new_string = "".join(new_list)
    return new_string
