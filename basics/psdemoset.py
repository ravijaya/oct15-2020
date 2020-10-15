"""set vs list, """

# unique unordered collections of elements

items = set([1.2, .98, 'pam', 'jane', 4, 5])
# items = frozenset(items)  # immutable
items.add(12)
items.add('pam')

items.remove('pam')
print(items)

for item in items:
    print(item)