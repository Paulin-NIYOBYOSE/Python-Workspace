#A lambda function is a single-expression anonymous function.
#Anonymous: They don’t have a name (unless you assign them to a variable).
# Single Expression: The body of a lambda is a single expression, not a block of statements.
# Quick to Define: Ideal for short, throwaway functions.

numbers = [1,2,3,4,5]
squared = list(map(lambda x: x**2, numbers))
print(squared)

#using lambda as sorting keys
data = [{'name': 'Paulin', 'age': 18}, {'name':'shem', 'age': 26},{'name': 'Niyobyose', 'age': 19}]
sorted_data = sorted(data, key=lambda k: k["age"])
print(sorted_data)

#using lambda in callbacks

#short-term utility functions with lambda
result = (lambda x,y: x*y)(2,3)
print(result(2,3))
#
#  Advantages
# Conciseness: Quick to write for simple operations.
# Readability: Helps in avoiding verbose(overdetailed codes) code in some contexts.
# Flexibility: Can be used wherever a function is required as an argument.
#
#  Limitations
# Single Expression: Cannot contain multiple statements or assignments.
# Reduced Readability: Overuse in complex logic can make the code harder to read.
# Debugging: Difficult to debug since they lack names and proper context.
#
# Best Practices
# Use lambda functions for short and simple tasks.
# Avoid lambdas when the function logic is complex or spans multiple lines.
# Provide meaningful variable names for lambdas when assigned.
