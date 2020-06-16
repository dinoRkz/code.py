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
    # define some starting values
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b)
    
    s = "This is a string"
    print(s)
    
    # Combining them will cause an error
    # print(s+b)
    
    # Bytes and strings need to be properly encoded and decoded
    # before you can work on them together
    s2 = b.decode('utf-8')
    print(s+s2)
    
    b2 = s.encode('utf-8')
    print(b+b2)
    
    # encode the string as UTF-32
    b3 = s.encode('utf-32')
    print(b3)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()