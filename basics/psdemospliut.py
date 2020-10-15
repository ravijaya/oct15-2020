s = 'root:x:0:0:root:/root:/bin/bash'

items = s.split(':')
print(items)
print()

print(s.split(':')[0])  # indexing
print()

print(s.split(':')[1:])  # slicing
print()

# iterator

for item in s.split(':')[1:]:  # iteration
    print(item)