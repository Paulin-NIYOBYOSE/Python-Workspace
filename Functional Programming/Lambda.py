#A lambda function is a single-expression anonymous function.
#Anonymous: They don’t have a name (unless you assign them to a variable).
# Single Expression: The body of a lambda is a single expression, not a block of statements.
# Quick to Define: Ideal for short, throwaway functions.

numbers = [1,2,3,4,5]
squared = list(map(lambda x: x**2, numbers))
print(squared)