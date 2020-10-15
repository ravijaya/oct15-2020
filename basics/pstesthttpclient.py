import requests

url = 'http://google.com/data'
response = requests.get(url)
print(response.status_code)
print()
print(response.headers)
print()
# print(response.content)
print(response.text)