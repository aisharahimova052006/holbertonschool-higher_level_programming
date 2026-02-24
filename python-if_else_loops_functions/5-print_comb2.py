#!/usr/bin/python3
i = 0
j = 0
string = ''
for n in range(0, 99):
    i = n // 10 
    j = n % 10  
    str = "{}{}".format(i, j)  
    print(str, end=', ')  
    print('99', end='\n')
