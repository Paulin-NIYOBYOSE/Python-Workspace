# Raising a ValueError
def divide(a, b):
    if b == 0:
        raise ValueError("You cannot divide by zero!")
    return a / b

divide(5, 0)  # This raises a ValueError.