#!/usr/bin/python3

"""
Module Docstring
"""

__author__ = "Dinesh Tumu"
__version__ = "0.1.0"
__license__ = "MIT"


# imports


# init variables

# assigning variables to a function
var_1 = range(10)

def main():
    """ Main entry point of the app """

    print("\nWhile Loops\n")
    # while expression:
    #     statement(s)

    iter_1 = 0
    while (iter_1 < 10):
        iter_1 += 1
        print("{}".format(iter_1), end = " ")
    else:
        print("\nLoop ended with iter_1 = {}".format(iter_1))

    iter_2 = 0
    while iter_2 < 10:
        print("{}".format(iter_2), end = " ")
        iter_2 += 1
    else:
        print("\nLoop ended with iter_2 = {}".format(iter_2))

    iter_3 = 0
    while iter_3 in var_1:
        print("{}".format(iter_3), end = " ")
        iter_3 += 1
    else:
        print("\nLoop ended with iter_3 = {}".format(iter_3))

    iter_4 = 0
    while iter_4 < 5:
        iter_4 += 1
        if iter_4 > 3: break
        if iter_4 == 2: continue
        print(f'{iter_4} ')

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()