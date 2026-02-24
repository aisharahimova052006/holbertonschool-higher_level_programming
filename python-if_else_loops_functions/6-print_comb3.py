#!/usr/bin/python3
i = 0
j = 0
string = ''
for n in range(0, 89):
    i = n // 10
    j = n % 10
    if i < j:
        str = "{}{}".format(i, j) 
        print(str, end=', ') 
    elif i == j:
        continue
    else:
        continue
print('89', end='\n')
