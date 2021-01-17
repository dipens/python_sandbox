# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['John', 'Paul', 'Sara', 'Susan']
for person in people:
    print(f'Current Person: {person}')


for person in people:
    if(person == 'Sara'):
        break
    print(f'Current Person: {person}')

for person in people:
    if(person == 'Sara'):
        continue
    print(f'Current Person: {person}')


for i in range(len(people)):
    print(people[i])

for i in range(0, 11):
    print(i)


count = 0
while count <= 50:
    print(count)
    count += 1
# While loops execute a set of statements as long as a condition is true.
