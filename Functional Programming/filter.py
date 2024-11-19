#filter: filters elements based on a specific condition and returns an iterable of elements that satisfy the condition
#filtering odd numbers using filter
numbers = [1,2,3,4,5,6,7,8]
odd_numbers = filter(lambda x: x % 2 != 0, numbers)
print(list(odd_numbers))

#filtering even numbers without using lambda function
def is_even(n):
    return n%2 ==0
even_numbers = filter(is_even, numbers)
print(list(even_numbers))