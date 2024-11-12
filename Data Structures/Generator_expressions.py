#A generator expression is similar to a list comprehension but instead
#                       of creating a full list in memory, it creates an iterator that yields
#                       items one at a time. This makes it more memory-efficient, especially
#                       for large datasets, whereas a list comprehension creates and stores
#                       the entire list in memory.

#Syntax of a generator expression
#(expression for item in iterable if condition)
gen = (x * x for x in range(5))
# print(gen)#prints generator object instead of a list
# print(next(gen))#0
# print(next(gen))#1

# printing all values from a generator
for i in gen:
    print(i)

nums = [1, 2, 3, 4, 5, 6]
squares_gen = (num * num for num in nums if num % 2 == 0)
for square in squares_gen:
    print(square)

#comparison with list expressions
# 1.list expressions
#Syntax: [expression for item in iterable if condition]
#Creates the entire list in memory.

squares = [num * num for num in nums if num % 2 == 0]
print(squares)

# 2.generator expressions
#Syntax: (expression for item in iterable if condition)
#Doesn’t create the entire list but returns an iterator (generator).
squares_ge = (num * num for num in nums if num % 2 == 0)

# Example od expression
numbers = [1, 2, 3, 4, 5]
sum_of_squares= sum(x * x for x in numbers)
print(sum_of_squares)






