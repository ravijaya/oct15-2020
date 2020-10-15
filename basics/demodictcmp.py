apps1 = {
    'web server': 'apache httpd',
    'db': 'mongodb',
    'wsgi': 'uwsgi'
}

apps2 = {
    'web server': 'tomcat',
    'db': 'mongodb',
    'wsgi': 'uwsgi'
}

# print(apps1 == apps2)

x = set(apps1.items())
y = set(apps2.items())
print(x.intersection(y))
print(dict(x.intersection(y)))
print(x & y)

print(x.difference(y))
print(y - x)