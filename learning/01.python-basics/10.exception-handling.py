#!/usr/bin/python3

"""
Module Docstring
"""

__author__ = "Dinesh Tumu"
__version__ = "0.1.0"
__license__ = "MIT"


# imports
import sys

# init variables


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

    # generator
    i = start
    while i <= stop:
        yield i
        i += step


def main():
    """ Main entry point of the app """

    # Simple Exception Handling
    try:
        var_1 = 5/0
    except ValueError:
        print("Found Value Error")
    # except ZeroDivisionError:
    #     print("Don't divide by zero")
    except:
        print(f'Unknown Error: {sys.exc_info()[1]}')
    else:
        print("No error found")
        print(var_1)

    # Reporting errors in functions and classes
    try:
        for i in inclusive_range(25,2,3,4):
            print(i, end = ' ')
        print()
    except TypeError as e:
        print(f'range error: {e}')

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()