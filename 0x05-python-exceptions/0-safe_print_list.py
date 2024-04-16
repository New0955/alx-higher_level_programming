#!/usr/bin/python3
""" function that prints x elements of a list  """
def safe_print_list(my_list=[], x=0):
    num = 0;
    try:
        for index in range(x):
            print("{}".format(my_list[index]), end="")
            num += 1
    except IndexError:
        pass
    print()
    return (num)

