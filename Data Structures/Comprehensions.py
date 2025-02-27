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
# print(positive_nums)
# print(negative_nums)
# print(even_nums)
# print(odd_nums)

grades = [85, 42, 79, 90, 56, 61, 30]
passing = [ grade for grade in grades if grade >60 ]
# print(passing)

#comprehension exercises
#Given a list of numbers, generate a list of squares for only the even numbers.
my_list = [1, 2, 3, 4, 5, 6]
square_of_even_numbers = [num * num for num in my_list if num % 2 == 0]
# print(square_of_even_numbers)

#extract vowels
word = "comprehension"
vowels = "aeiuo"
vowels_in_word = [char for char in word if char in vowels]

#generate unique characters
my_word = "banana"
unique_chars = {char for char in my_word} # remember to use set comprehension instead of list comprehension
# print(unique_chars)

#capitalize words
word_to_captilise = "Paulin"
word_in_capital = [char.upper() for char in word_to_captilise]
# print(word_in_capital)
words = ["python", "list", "comprehension"]
capitalized_words = [word.upper() for word in words]
# print(capitalized_words)

#filter divisible by 3
divisible_by_3 = [num for num in range(1,11) if num % 3 == 0]

#dictionary exercises
#square dictionary
squares_dict = {num: num**2 for num in range(1,11)}
# print(squares_dict)

#wordlength dictionary
words = ["apple", "mango", "banana", "guava"]
word_lengths = {word: len(word) for word in words}
# print(word_lengths)

#set comprehensions
numbers = [1, 2, 2, 4, 6, 6, 7, 8, 9, 10]
unique_squares = {num ** 2 for num in numbers }
print(unique_squares)

#finding palindromes
my_words =["level", "python", "radar", "hello", "madam"]
palindromes = [word for word in my_words if word[::-1] == word]
# print(palindromes)