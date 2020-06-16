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
    # stack implementation using python lists
    stack = [] 

    # append() function to push element in to the stack 
    stack.append('1') 
    stack.append('2') 
    stack.append('3')
    stack.append('4') 

    print('Initial stack') 
    print(stack) 

    # pop() fucntion to pop element from stack in LIFO order 
    print('\nElements poped from stack:') 
    print(stack.pop()) 
    print(stack.pop()) 
    print(stack.pop()) 

    print('\nStack after elements are poped:') 
    print(stack) 

    # uncommenting print(stack.pop()) 
    # will cause an IndexError 
    # as the stack is now empty 

main()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()