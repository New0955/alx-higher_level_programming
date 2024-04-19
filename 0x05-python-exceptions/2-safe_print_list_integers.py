#!/usr/bin/python3

""" function that prints the first x elements of a list and only integers """
def safe_print_list_integers(my_list=[], x=0):
    num = 0
    for item in range(x):
        try:
            print("{:d}".format(my_list[item]), end="")
            num += 1
        except (ValueError, TypeError):
            pass
    print()
    return num

