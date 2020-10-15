items = {'host': 'ws1',
         'domain': 'rootcap.in'}

print(items)
#print(type(items))
#print(len(items))
print()

items['desc'] = 'web server'  # adding
print(items)
print()

items['host'] = 'ws3'  # update
print(items)
print()

# value = items.pop('domain')  # delete
# print(value)
# print(items)

for key, value in items.items():  # iterate
    print(key, '->', value)
