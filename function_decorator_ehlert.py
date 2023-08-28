"""
Program Name: function_decorator_ehlert.py
Author: Tony Ehlert
Date: 8/28/2023

Program Description: This program contains a function that has a decorator applied that makes it run twice
"""
def base_function():
    """
    This function simply prints a statement to the console
    :return: None
    """
    print("Do it Twice Function Decorator Assignment!")

def function_decorator(func):
    """
    This is a simple decorator function that wraps a base function and makes it run twice
    :param func: base function to be run twice
    :return: None
    """
    def wrapper():
        func()
        func()
    return wrapper

base_function = function_decorator(base_function)

if __name__ == "__main__":
    base_function()