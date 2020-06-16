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
    # tuples are immutable - can't be modified (no append and delete as well) after creating them
    tuple_1 = (1, 2, 3, 4)
    print(tuple_1)

    # lists are mutable - can modify, append, delete etc. after creating them
    list_1 = [1, 2, 3, 0, 5, 6]
    # use any() and all() to test sequences for boolean values
    # any will return true if any of the sequence values are true
    print(any(list_1))
    
    # all will return true only if all values are true
    print(all(list_1))
    
    # min and max will return minimum and maximum values in a sequence
    print("min: ", min(list_1))
    print("max: ", max(list_1))    
    
    # Use sum() to sum up all of the values in a sequence
    print("sum: ", sum(list_1))

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()