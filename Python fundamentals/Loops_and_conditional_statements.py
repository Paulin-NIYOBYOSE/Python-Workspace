#is statement
age = float(input("Enter your age: "))
if age < 18:
    print("you are under age")
elif age == 18:
    print("You are exactly 18 ")
else:
    print("you are over 18")

#logical operators
name = input("Enter your name: ")
isRich = True

if name == "Paulin" and isRich:
    print("Welcome boss")
else:
    print("You are not eligible to enter the system")

#Loops
fruits = ["apple","banana","guava"]
for fruit in fruits:
    print(fruit)

#while
number = 0
while number < 10:
    print(number)
    number += 1 #increment number to avoid infinite loop

#break and continue
for i in range(0,10):
    if i == 5:
        break #exits the loop when i = 5
    print(i)
for i in range(10):
    if i == 5:
        continue #skip 5
    print(i)

