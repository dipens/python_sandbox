# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
import json
import urllib.request

with urllib.request.urlopen("https://api.github.com/users") as url:
    data = json.loads(url.read().decode())
    for user in data:
        print(user['login'])
userJSON = '{"first_name": "John", "last_name": "Doe", "age":30}'

user = json.loads(userJSON)


print(user['first_name'])


car = {'make': 'Ford', 'model': 'Mustang', 'year': '1970'}
carJSON = json.dumps(car)
print(carJSON)
