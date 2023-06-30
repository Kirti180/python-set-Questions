def add_person(dictionary, name, age):
    dictionary[name] = age

def update_age(dictionary, name, new_age):
    if name in dictionary:
        dictionary[name] = new_age

def delete_person(dictionary, name):
    if name in dictionary:
        del dictionary[name]

# Create an empty dictionary
people = {}

# Add a new name-age pair
add_person(people, "John", 25)
print(people)

# Update the age of a name
update_age(people, "John", 26)
print(people)

# Delete a name from the dictionary
delete_person(people, "John")
print(people)
