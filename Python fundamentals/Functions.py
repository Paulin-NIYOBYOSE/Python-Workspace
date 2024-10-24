def greet(name):
    return f"Hello {name}"
Message = greet("Paulin")
print(Message)

#default parameters
def multiply(a, b=2): #b has a default parameter as 2
    return a * b
print(multiply(5)) #multiplies 5 with the default parameter 2
print(multiply(3,4))# multiplies 3 with 4

#args and kwargs
def add_numbers(*args):# args allows you to pass a variable number of non-keyword arguments.
    return sum(args)
print(add_numbers(1,2,3,4))

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name= "Paulin", age = 18)

#lambda function
square = lambda x: x * x
print(square(5))

#function annotations
def add(a: int, b: int) -> int:
    return a + b

result = add(5, 3)  # result is inferred to be of type int

#documentation strings
def add(a: int, b: int) -> int:
    """Add two integers and return the sum.

    Args:
        a (int): The first integer to add.
        b (int): The second integer to add.

    Returns:
        int: The sum of the two integers.
    """
    return a + b

# Accessing the docstring
print(add.__doc__)


#closure functions

def outer_function():
    message = "Hello this is a message"

    def inner_function():
        return message
    return inner_function
closure_func = outer_function()
print(closure_func())
