#!/usr/bin/python3
def print_reversed_list_integer(mylist=[]):  # noqa: E251
    mylist = mylist[::-1]
    i = 0
    length = len(mylist)
    for i in range(i, length):
        string = "{:d}".format(mylist[i])
        print(string, end='\n')
