# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Dipen'
age = 30

print('Hello, my name is ' + name + ' and I am ' + str(age))
# String Formatting

print('My name is {name} and I am {age}'.format(name=name, age=age))


# F-String

print(f'Hello my name is {name} and I am {age}')
# String Methods
s = 'helloworld'
print(s.capitalize())


print(s.upper())

print(s.lower())


print(s.swapcase())

print(len(s))


print(s.replace('world', 'everyone'))

sub = 'o'
print(s.count(sub))
print(s.endswith('d'))
print(s.split(','))
print(s.find('z'))
print(s.isalnum())
print(s.isalpha())
print(s.isnumeric())
