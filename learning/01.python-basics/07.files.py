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
    # Open a file for writing and create it if it doesn't exist
    f = open("textfile.txt","w+")

    # Open the file for appending text to the end
    # f = open("textfile.txt","a+")

    # write some lines of data to the file
    for i in range(10):
        f.write("This is line %d\r\n" % (i+1))

    # close the file when done
    f.close()

    # Open the file back up and read the contents
    f = open("textfile.txt","r")
    if f.mode == 'r': # check to make sure that the file was opened
        # use the read() function to read the entire file
        # contents = f.read()
        # print (contents)
        fl = f.readlines() # readlines reads the individual lines into a list
        for x in fl:
            print (x)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()