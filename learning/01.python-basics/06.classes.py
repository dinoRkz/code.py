#!/usr/bin/python3

"""
Module Docstring
"""

__author__ = "Dinesh Tumu"
__version__ = "0.1.0"
__license__ = "MIT"

# imports

# init variables

class myClass():
  def method1(self):
    print ("myClass method1")
    
  def method2(self, someString):
    print ("myClass method2: " + someString)
    
class anotherClass(myClass):
  def method2(self):
    print ("anotherClass method2")
    
  def method1(self):
    myClass.method1(self)       # inherited
    print ("anotherClass method1")
      
def main():
    """ Main entry point of the app """
    c = myClass()
    c.method1()
    c.method2("This is a string")

    c2 = anotherClass()
    c2.method1()
    c2.method2("This is a string")      # not inherited in this case

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()