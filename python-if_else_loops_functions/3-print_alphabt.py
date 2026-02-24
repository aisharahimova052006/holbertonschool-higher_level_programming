#!/usr/bin/python3
i = 97
str = ''
while i < 123:
    str += chr(i)
    i = i + 1
str = str.replace('e', '')
str = str.replace('q', '')
print("{}".format(str), end='')
