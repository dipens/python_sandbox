# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules
import datetime
from datetime import date
import time
from time import time
from camelcase import CamelCase
from validator import validate_email

today = date.today()
print(today)

timestamp = time()
print(timestamp)

c = CamelCase()


print(c.hump('hello world'))


email = 'test#test.com'
if validate_email(email):
    print('Email is valid')
else:
    print('Email is not valid')
