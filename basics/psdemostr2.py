name, age = 'sarah', 3

print('i am name, age years old')
print()
print(f'i am {name}, {age} years old')  # formatted string
print()
print(f'i am {name.title()}, {age * 3} years old')
print()

file_path = 'c:\templates\neon\folder99\balances\rules\temp.txt'
print(file_path)
print()

file_path = r'c:\templates\neon\folder99\balances\rules\temp.txt'  # raw string
print(file_path)
print()

from sys import getsizeof
s = b'python'
print(s)
print(getsizeof(s))
print(type(s))
print(s.decode())   # convert bytes into str
print()
s = 'python'
print(s.encode())   # convert str into bytes