# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries


# Create dict
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

print(person, type(person))


# Use cons
person2 = person.copy()
person2['city'] = 'boston'

print(person.get('first_name'))
print(person['last_name'])
person['phone'] = '123'
print(person)


print(person.keys())
print(person2)


del person['age']
print(person)


print(len(person))


people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25},
]

print(people[1]['name'])
