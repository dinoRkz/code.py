#!/usr/bin/python3

"""
Module Docstring
"""

__author__ = "Dinesh Tumu"
__version__ = "0.1.0"
__license__ = "MIT"


# imports


# init variables



def main():
    """ Main entry point of the app """

    # Type conversion
    a = "a"
    b = 10
    c = "1001"
    print(bin(b))
    print(oct(b))
    print(hex(b))
    print(ord(a))
    # The int() function takes second argument as the base of the number to be converted
    print(int(c,2))
    print(int(c,10))

    # str(b)
    # tuple(list)
    # list(tuple)
    # set(list)

    # input
    a, b = input().split()
    a = int(a)
    b = float(b)
    # a, b = int(input("Input Numbers here: ").split())

    # print
    # str.format()
    print("{}, {}".format(a, b))

    # f string
    print(f"{a}, {b}")

    # any, all
    list_1 = [1, 2, 3, 0, 5, 6]
    # use any() and all() to test sequences for boolean values
    # any will return true if any of the sequence values are true
    print(any(list_1))
    # all will return true only if all values are true
    print(all(list_1))


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()