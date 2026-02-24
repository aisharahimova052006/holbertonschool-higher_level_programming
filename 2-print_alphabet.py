#!/usr/bin/python3
i = 97
str = ''
while i < 123:
    str = str + chr(i) + ''
    i = i + 1
print("{}".format(str), end='')
