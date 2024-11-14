# What is an Exception?
# An exception is an event that disrupts the normal flow of a program’s execution.
# For example, trying to divide by zero, accessing a file that doesn’t exist,..


try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Code that runs if a ZeroDivisionError occurs
    print("You can't divide by zero!")

#catching multiple exceptions
try:
    my_string = int("I am not a number")
    print(my_string)
except (ValueError, TypeError):
    print("Caught a value or type error")

#Using else
try:
    result = 10 / 2
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("The division was successful!")

#using finally
try:
    file = open("sample.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    file.close()

#Catching custom exceptions
class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom error!")
except CustomError as e:
    print(e)

#Nested try/except blocks
try:
    result = 10 / 2
    try:
        file = open("sample.txt", "r")
    except FileNotFoundError:
        print("File not found inside nested try block.")
except ZeroDivisionError:
    print("Division by zero in outer block.")
#Best Practices
# Use specific exceptions: Avoid generic except statements unless you’re logging or re-raising the exception.
# Keep try blocks short: Only include code that could raise an exception.
# Use custom exceptions when needed: For handling specific errors in your application.




