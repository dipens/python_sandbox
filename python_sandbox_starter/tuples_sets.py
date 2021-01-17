# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

fruits = ('Apples')
fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

print(fruits)
print(fruits[1])


print(len(fruits))


# A Set is a collection which is unordered and unindexed. No duplicate members.

fruits_set = {'Apples', 'Oranges', 'Mango'}

print('Apples' in fruits_set)


# Add to set
fruits_set.add('Grape')
fruits_set.add('Grape')
fruits_set.discard('Oranges')

print(fruits_set)
print(fruits_set)
