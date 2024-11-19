#reduce: cumulatively applies a binary function to elements of the iterable and returns a single value resulting from applying the function
from functools import reduce

#finding the maximum number using reduce
numbers = [1,2,3,4,5,6,7,8,9]
max_number = reduce(lambda x,y: x if x>y else y, numbers)
print(max_number)

#finding sum using reduce
def add(x,y):
    return x + y
sum = reduce(add, numbers)
print(sum)

#finding max value without lambda
def find_max(x,y):
    return x if x>y else y
big_number = reduce(find_max,numbers)
print(max(numbers))


#summary about all
# filter(): Use when you need to exclude elements based on a condition.
# For example, filtering out invalid values or selecting specific items from a dataset.

# map(): Use when you want to transform every element in an iterable
# (e.g., modifying or processing data, like formatting strings, squaring numbers, etc.).

# reduce(): Use when you want to combine the elements of an iterable into a single result,
# such as calculating a sum, product, or finding the maximum.

