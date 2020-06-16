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
    # range is a generator as well 
    # this function is a modified version of range
    for i in inclusive_range(25):
        print(i, end = ' ')
    print()

def inclusive_range(*args):
    numargs = len(args)
    start = 0
    step = 1
    
    # initialize parameters
    if numargs < 1:
        raise TypeError(f'expected at least 1 argument, got {numargs}')
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else: raise TypeError(f'expected at most 3 arguments, got {numargs}')

    # generator code
    i = start
    while i <= stop:
        # to return this value to the main function
        yield i 
        i += step

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()