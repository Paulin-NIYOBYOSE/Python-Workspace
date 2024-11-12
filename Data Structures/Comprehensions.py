#list comprehension => a concise way to create lists in python
#                      compact and easier to read than traditional loops
#                       [expression for value in iterable if condition]
# traditional way
double = []
for x in range(1,11):
    double.append(x*2)
print(double)

#using list comprehension
doubles = [x * 2 for x in range(1,11)]
triples = [y * 3 for y in range(1,11)]
squares = [z * z for z in range(1,11)]
# print(squares)

#strings
fruits = ["apple", "mango", "banana", "guava"]
# fruits = [fruit.upper() for fruit in fruits]
fruit_charts = [fruit[0] for fruit in fruits]
# print(fruit_charts)

#conditions
numbers = [1, -2, 3, -4, 5, -6, 8, -7 ]
positive_nums = [num for num in numbers if num>=0 ]
negative_nums = [num for num in numbers if num>=0 ]
even_nums = [num for num in numbers if num % 2 == 0 ]
odd_nums = [num for num in numbers if num %2 == 1 ]
print(positive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)

grades = [85, 42, 79, 90, 56, 61, 30]
passing = [ grade for grade in grades if grade >60 ]
print(passing)

