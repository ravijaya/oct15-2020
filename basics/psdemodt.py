from datetime import datetime
from time import mktime
from glob import glob
from os import listdir
from os.path import join

content = {}

for dir_name in glob('temp/*'):
    ts_string = dir_name.lstrip('temp/xxx-')
    # print(datetime.strptime(ts_string, '%d-%m-%Y--%H-%M-%S-%f'))
    ts = mktime(datetime.strptime(ts_string, '%d-%m-%Y--%H-%M-%S-%f').timetuple())
    content[dir_name] = ts

# datetime.strftime()

# print(sorted(content.items(), key=lambda items: items[1]))
# print(sorted(content.items(), key=lambda items: items[1])[0])
dir_name, unix_ts = sorted(content.items(), key=lambda items: items[1])[-1]
print(f'reading the directory : {dir_name}')

for filename in listdir(dir_name):
    print(filename.center(80, '-'))
    abs_path = join(dir_name, filename)
    print(open(abs_path).read())
    print()
