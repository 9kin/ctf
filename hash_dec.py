"""pyhashcat
os : unix
by : 9kin https://github.com/9kin
thanks to
    hashcat https://hashcat.net/hashcat/
"""

import subprocess

def ex(command):
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    return stdout

def version():
    return ex("hashcat --version").decode().replace('\n', '')

def help():
    return ex("hashcat --help").decode()

print(version())
print(help())

