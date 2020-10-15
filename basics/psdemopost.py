"""single threaded http client"""


import requests
from time import perf_counter

url = 'https://reqres.in/api/users'
payload = [('tim', 'manager'), ('nat', 'director'), ('pat', 'clerk'), ('nick', 'helper')]
names = ['name', 'job']

start = perf_counter()

for person in payload:
    data = dict(zip(names, person))
    res = requests.post(url, json=data)
    print(res.status_code)
    print()
    print(res.json())

print(perf_counter() - start)


# concurrency
    # multi threading
    # multi processing 
