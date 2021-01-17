# Python has functions for creating, reading, updating, and deleting files.
myFile = open('myFile.txt', 'a')


print('Name: ', myFile.name)
print('Is closed: ', myFile.closed)
print('Mode: ', myFile.mode)


myFile.write('I like Python\n')
myFile.write(' and JS\n')
myFile.close


myFile = open('myFile.txt', 'r+')
text = myFile.read(100)
print(text)
