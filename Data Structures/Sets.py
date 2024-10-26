# Creating a set of fruits
fruits = {"apple", "banana", "cherry", "orange"}
print("Initial set of fruits:", fruits)

# Adding a new fruit to the set
fruits.add("mango")
print("Set after adding a new fruit:", fruits)

# Removing an element from the set
fruits.remove("banana")
print("Set after removing 'banana':", fruits)

# Discarding an element from the set
fruits.discard("banana")  # Won't cause an error if 'banana' isn't found
print("Set after trying to discard 'banana' again:", fruits)

# Checking if an element is in the set
is_apple_in_fruits = "apple" in fruits
print("Is 'apple' in the set?", is_apple_in_fruits)

# Union of two sets
tropical = {"mango", "pineapple", "papaya"}
all_fruits = fruits.union(tropical)
print("Union of fruits and tropical sets:", all_fruits)

# Intersection of two sets
common_fruits = fruits.intersection(tropical)
print("Intersection of fruits and tropical sets:", common_fruits)

# Difference of two sets
unique_fruits = fruits.difference(tropical)
print("Fruits that are not tropical:", unique_fruits)

# Clearing all elements from the set
fruits.clear()
print("Set after clearing all elements:", fruits)
