#!/usr/bin/python3
def write_file(filename="", text=""):
    """Write a string to a UTF8 text file and return the number of characters written."""
    with open(filename, "w", encoding="utf-8") as f:
        count = f.write(text)
    return count
