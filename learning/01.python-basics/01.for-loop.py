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
var_2 = range(3, 10)
var_3 = range(3, 10, 2)

string = "dino"
list_1 = [3, 2, 1]
inf = float('inf')
list_2 = [[0,1,4,inf,3], [1,0,2,inf,4], [4,2,0,1,5], [inf,inf,1,0,3], [3,4,5,3,0], [3,4,inf,3,0]]
list_3 = [ (1, (2, 3)), (4, (5, 6)), (7, (8, 9))]



def main():
    """ Main entry point of the app """

    print("\nFor Loops\n")
    # for iterating_var in sequence:
    #     statement(s)

    for idx, item in enumerate(var_1):
        # print(item, end =" ") :this statement is equivalent to the one below
        print("[{}, {}]".format(idx, item), end = " ")
    else:
        print("\nFinite loop 1 ended with iterator = {}\n".format(idx))
    # print here for the newline

    for idx, item in enumerate(var_2):
        print("[{}, {}]".format(idx, item), end = " ")
    else:
        print("\nFinite loop 2 ended with iterator = {}\n".format(idx))

    for idx, item in enumerate(var_3):
        print("[{}, {}]".format(idx, item), end = " ")
    else:
        print("\nFinite loop 3 ended with iterator = {}\n".format(idx))

    for idx, char in enumerate(string):
        print("[{}, {}]".format(idx, char), end = " ")
    else:
        print("\nFinite loop 4 ended with iterator = {}\n".format(idx))

    for idx, item in enumerate(list_1):
        print("[{}, {}]".format(idx, item), end = " ")
    else:
        print("\nFinite loop 5 ended with iterator = {}\n".format(idx))

    # format() works only for string, so "<something_here>".format(val) works
    for idx_1, row in enumerate(list_2):
        for idx_2, val in enumerate(row):
            print("{:4}".format(val), end = "")
        else:
            print("\nRow {} printed".format(idx_1 + 1))
    else:
        print("\nFinite nested loop 6 i.e., Matrix with {} rows and {} colomns printed\n".format(idx_1 + 1, idx_2 + 1))
    # one-line way of simply printing the matrix: print('\n'.join([''.join(["{:4}".format(item) for item in row]) for row in list_2]))

    for idx, item in enumerate(list_3):
        print("[{}, {}]".format(idx, item), end = " ")
    else:
        print("\nFinite loop 7 ended with iterator = {}\n".format(idx))

    for idx, (item_1, item_2) in enumerate(list_3):
        print("[{}, {}, {}]".format(idx, item_1, item_2), end = " ")
    else:
        print("\nFinite loop 8 ended with iterator = {}\n".format(idx))

    for idx, (item_1, (item_2, item_3)) in enumerate(list_3):
        print("[{}, {}, {}]".format(item_1, item_2, item_3), end = " ")
    else:
        print("\nFinite loop 9 ended with iterator = {}\n".format(idx))                


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()