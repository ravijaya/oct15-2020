from os import listdir
from os.path import join, isfile, isdir, getsize, getmtime, splitext, basename, dirname
from time import ctime
from sys import argv

print(argv)
print(argv[0])
print(dirname(argv[0]))
print(basename(argv[0]))
print(splitext(basename(argv[0])))
exit()
# path = r'c:\users\uid\documents'
path = '/tmp'


temp = listdir(path)[0]
abs_path = join(path, temp)
print(abs_path)
print()
print(isdir(abs_path))
print(isfile(abs_path))
print()
print(getsize(abs_path))
print(getmtime(abs_path))
print(ctime(getmtime(abs_path)))



