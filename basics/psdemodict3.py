items = {'host': 'ws1',
         'domain': 'rootcap.in',
         }

apps = {
    'web server': 'apache httpd',
    'db': 'mongodb',
    'wsgi': 'uwsgi'
}

print({**items, **apps})
print(dict(**items, **apps))
print(dict())


# def demo(**kwargs):
#     print(kwargs)
#
#
# demo(host='ws9', domain='sample.com')
# demo(**items, **apps)