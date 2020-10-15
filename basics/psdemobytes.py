from sys import platform
from subprocess import check_output


if platform == 'win32':
    cmd = ['ipconfig']
elif platform in ['linux', 'darwin']:
    cmd = ['/sbin/ifconfig']

op = check_output(cmd)
print(op.decode())