#!/usr/bin/python3

"""
Module Docstring
"""

__author__ = "Dinesh Tumu"
__version__ = "0.1.0"
__license__ = "MIT"


# imports
from string import Template

# init variables



def main():
    """ Main entry point of the app """
    



    # Template Strings
    # Simple variable substitution, much easier to use, effective and the code is more readable. 
    # Control the output formatting with all kinds of specifiers for spacing, 
    # number formatting, justification and so on
    
    # Usual string formatting with format()
    str1 = "You're watching {0} by {1}".format("Advanced Python", "Joe Marini")
    print(str1)
    
    # create a template with placeholders
    templ = Template("You're watching ${title} by ${author}")
    
    # use the substitute method with keyword arguments
    str2 = templ.substitute(title="Advanced Python", author="Joe Marini")
    print(str2)
    
    # use the substitute method with a dictionary
    data = { 
        "author": "Joe Marini",
        "title": "Advanced Python"
    }
    str3 = templ.substitute(data)    
    print(str3)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()