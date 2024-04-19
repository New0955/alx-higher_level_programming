#!/usr/bin/python3
""" function that divides 2 integers and prints the result """
def safe_print_division(a, b):
    try:
        division = a / b
    except (TypeError, ValueError, ZeroDivisionError):
        division = None
    finally:
        print("Inside result: {}\n".format(division), end="")
        return division

