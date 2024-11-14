# What is an Exception?
# An exception is an event that disrupts the normal flow of a program’s execution.
# For example, trying to divide by zero, accessing a file that doesn’t exist,..


try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Code that runs if a ZeroDivisionError occurs
    print("You can't divide by zero!")