#!/usr/bin/python3
class Square:
    def __init__(self, size=o):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValeError("size must be >= 0")
        self.__size = size


