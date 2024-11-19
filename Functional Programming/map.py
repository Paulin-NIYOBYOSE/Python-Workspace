#map:applies a function to every element in the iterable and returns an iterable of transformed elements

#doubling numbers using map:
numbers = [1,2,3,4,5,6,7]
doubled_numbers = map(lambda x: x * 2, numbers)
squared_numbers = map(lambda x: x ** 2, numbers)
doubled_numbers_list = list(doubled_numbers)
print("doubled_numbers" + str(doubled_numbers_list))
print(list(squared_numbers))

#doubling numbers without using lambda function
#function to double number

def double(n):
    return n * 2

doubled_numbers_without_lambda = map(double, numbers)
print(list(doubled_numbers_without_lambda))
