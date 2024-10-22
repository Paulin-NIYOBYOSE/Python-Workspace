# Creating variables
x = 5            # Integer
name = "Paulin"  # String
price = 19.99    # Float
is_active = True # Boolean

# Printing the variables
print(x)
print(name)
print(price)
print(is_active)

#dynamic typing
number = 10      # Initially, an integer
print(number)
number = "Ten"   # Now, a string
print(number)

#multiple variable assignment
a,b,c = 1,2,3
print(a,b,c)

#swapping variables
x,y = 10,5
x,y = y,x
print(x,y)


#type convention
x = "123"
y = int(x) #converts string to integer
print(y)

#checking variable type
age = 18
name= "Paulin"
networth = 1234567.8
is_rich = True
print(type(age))
print(type(name))
print(type(networth))
print(type(is_rich))


#scope of variables
def my_function():
    local_variable = "I am local variable"
    print(local_variable)

my_function()
#print(local_variable)# error because its a local variable

#global variables
global_variable = "I am global variable"

def another_function():
    print(global_variable)
another_function()

#global keyword helps us to modify a global variable inside a function
count = 0
def increment():
    global count
    count += 1
increment()#calling increment function
print(count)

#best practices
#snake case
first_name = "Paulin"
last_name = "Niyobyose"

def calculate_area(radius):
    pi = 3.14  # Keep pi close to its usage
    area = pi * (radius ** 2)
    return area

#exercises
#1Variable creation and printing
# Creating variables of different data types
integer_var = 42
float_var = 3.14
string_var = "Hello, World!"
boolean_var = True

# Printing the variables
print("Integer:", integer_var)
print("Float:", float_var)
print("String:", string_var)
print("Boolean:", boolean_var)

#2. String Manipulation
#Write a program that takes a user's name and age, and prints a greeting message using formatted strings.

name = input("Enter your name:")
age = input("Enter your age:")
greeting = f"Hello, {name}! You are {age} years old"
print(greeting)

#3. Arithmetic Operations
#Create a program that calculates the area and circumference of a circle given its radius.
radius = float(input("Enter your radius:"))
def circle_area_and_circumference(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    circumference = 2 * pi * radius
    return area, circumference
area, circumference = circle_area_and_circumference(radius)
print(f"Area: {area}")
print(f"Circumference: {circumference}")

#4. Simple Calculator
#Build a basic calculator that takes two numbers and performs addition, subtraction, multiplication, and division.
#Taking user inputs
number1 = float(input("Enter a number one:"))
number2 = float(input("Enter a number two:"))
operation = input("Enter operation(add, subtract, multiply, divide):")
#function for simple calc
def calculator (number1, number2, operation):
    if operation == "add":
        return number1 + number2
    if operation == "subtract":
        return number1 - number2
    if operation == "multiply":
        return number1 * number2
    if operation == "divide":
        return number1 / number2
    else:
        return "Invalid operation"
result = calculator(number1,number2, operation)
print(result)


