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
button.on_click(lambda: print("Button clicked!"))

