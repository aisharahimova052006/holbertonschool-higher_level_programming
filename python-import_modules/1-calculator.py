#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
c = add(a, b)
d = sub(a, b)
e = mul(a, b)
f = div(a, b)
string = "{} + {} = {}".format(a, b, c)
print(string)
string = "{} - {} = {}".format(a, b, d)
print(string)
string = "{} * {} = {}".format(a, b, e)
print(string)
string = "{} / {} = {}".format(a, b, f)
print(string)
if __name__ == "__main__":
    pass
