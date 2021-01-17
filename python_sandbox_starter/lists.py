# A List is a collection which is ordered and changeable. Allows duplicate members.


# Create a list
numbers = [1, 2, 3, 4]

numbers2 = list((1, 2, 3, 4, 5))
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']


print(numbers)
print(numbers2)
print(fruits[1])


# push array
fruits.append('Mangoes')
fruits.remove('Grapes')
fruits.pop(2)

fruits.insert(2, 'Cherry')
fruits.reverse()
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
