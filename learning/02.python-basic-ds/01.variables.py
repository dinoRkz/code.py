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
    var_1 = 7
    var_2 = 7.0
    var_3 = '7.0'
    var_4 = "7.0"
    var_5 = '''7.0'''
    var_6 = '''This is a string as well, 

            but it\'s multi line string'''
    var_7 = """It can be done in double 
            quotes as well"""
    var_8 = True
    var_9 = None
    var_10 = [1, 2, 3, 4, 5]
    var_11 = [[1, 2, 3], [4, 5, 6]]
    var_12 = (1, 2, 3)
    var_13 = { 'name' : 'dino', 'college' : 'nci'}
    var_14 = {1, 2, 3, 4}
    var_15 = bytes([0x41, 0x42, 0x43, 0x44])

    list = [var_1, var_2, var_3, var_4, var_5, 
            var_6, var_7, var_8, var_9, var_10, 
            var_11, var_12, var_13, var_14, var_15]

    for item in list:
        print('\'{}\' has ID: {} and type: {}'.format(item, id(item), type(item)))

    # there's no need for Python to create two different objects for the literal number '1'
    var_15 = (1, [2, 'True'])
    var_16 = 1
    print(id(var_12[0]), id(var_15[0]), id(var_16))
    if (var_12[0] is var_15[0]) and (var_12[0] is var_16) and (var_12[0] and var_16): 
        print("YES") 
    else: 
        print("NO")

    # To check if an object is of type 'something'
    if isinstance(var_12, tuple):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    """ This is executed when run from the command line """
    # variables, type, id
    main()