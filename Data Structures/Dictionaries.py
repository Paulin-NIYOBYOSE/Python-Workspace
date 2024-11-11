person = {
    "name": "Paulin",
    "age": 17,
    "profession": "AI Engineere"
}
print(person["name"])
print(person.get("age"))#Using get to access a dictionary
person["city"] = "Kigali"# Adding a new key value pair
print(person)
person["age"] = 18#updating the existing data
print(person["age"])
removed_profession = person.pop("profession")
print(removed_profession)#removing an item and returning its value

del person["city"]
print(person) #deletes an item

last_item = person.popitem()

