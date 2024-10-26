
# 1. Creating a list of names
names = ["Alice", "Bob", "Charlie", "Daisy", "Edward"]
print("Initial list of names:", names)

# 2. Adding a new name to the list
names.append("Frank")
print("List after adding a new name:", names)

# 3. Inserting a name at a specific index
names.insert(2, "George")
print("List after inserting a name at index 2:", names)

# 4. Removing a name from the list
names.remove("Alice")
print("List after removing a name:", names)

# 5. Accessing an element by its index
third_name = names[2]
print("The third name in the list is:", third_name)

# 6. Slicing the list to get the first three names
first_three_names = names[:3]
print("The first three names are:", first_three_names)

# 7. Finding the length of the list
list_length = len(names)
print("The number of names in the list is:", list_length)

# 8. Sorting the list in alphabetical order
names.sort()
print("List in alphabetical order:", names)

# 9. Reversing the list
names.reverse()
print("List in reverse order:", names)

# 10. Looping through each name in the list
print("All names in the list:")
for name in names:
    print(name)
