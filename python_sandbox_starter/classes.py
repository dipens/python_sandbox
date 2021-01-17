# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1
        return self.age


class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def setBalance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'


dipen = User('Dipen Shah', 'dipen@mail.com', 30)


print(dipen.name)
print(dipen.email)
print(dipen.age)
print(dipen.greeting())
print(dipen.has_birthday())
print(dipen.greeting())


janet = Customer('Janet', 'janet@mail.com', 25)
janet.setBalance(500)
print(janet.greeting())
print(janet.has_birthday())
print(janet.greeting())
