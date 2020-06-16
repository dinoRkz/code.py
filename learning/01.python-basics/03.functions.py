#!/usr/bin/python3

"""
Module Docstring
"""

__author__ = "Dinesh Tumu"
__version__ = "0.1.0"
__license__ = "MIT"


# imports


# init variables



# define basic function
def function_1():
    print("Printed from function_1()\n")

def function_2():
    print("Printed from function_2()\n")

def function_3():
    print("Printed from function_3()\n")

# function that takes arguments
def function_4(arg1, arg2):
    print (arg1, " ", arg2)

# function that returns a value
def cube(x):
    return x*x*x

# function with default value for an argument
# functions with default arguments should be at the end
def power(num, x=1):
    result = 1;
    for i in range(x):
        result = result * num  
    return result

# function with variable number of arguments. 
# *args should always be at the end
def multi_add(*args):
    result = 0;
    for x in args:
        result = result + x
    return result

def multi_func(*args):
    for item in args:
        item()

def fn_kw_args(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('{} : {}'.format(k, kwargs[k]))
    else: print('Meow.')

def main():
    """ Main entry point of the app """
    
    # Executes the function
    function_1()              
    
    # Executes the function and also prints 'None' as the function doesn't have any return type
    print(function_1())       
    print()

    # Prints the string representation of the function
    # Functions themselves are objects that can be passed around other pieces of python code
    print(function_1)         
    print()

    # Executes the function. If there is a return type, saves it in the variable
    var_0 = function_1()      
    print()

    # The string representation of the function is stored in the variable
    var_1 = function_1        
    var_2 = function_2
    var_3 = function_3

    functions_list = [function_1,function_2, function_3]
    for item in functions_list:
        # show the function reference
        print(item)
        # call the function
        item()

    function_4(10,20)
    print (function_4(10,20))
    print (cube(3))
    print (power(2))
    print (power(2,3))
    print (power(x=3, num=2))

    # args
    print (multi_add(4,5,10,4))
    print (multi_func(function_1, function_2, function_3))

    # kwargs - KeyWordARGumentS
    # ** unpacks dictionaries.
    # This 
    # func(a=1, b=2, c=3)
    # is the same as
    # args = {'a': 1, 'b': 2, 'c':3}
    # func(**args)

    fn_kw_args(name = 'xyz', college = 'abc', course = 'qwe')

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()