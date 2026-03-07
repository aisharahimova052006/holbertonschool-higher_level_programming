#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_c = []
    list_c = [x+y for x, y in zip(tuple_a, tuple_b)]
    if len(tuple_b) == 1 and len(tuple_a) == 1:
        c = tuple_a[0]+tuple_b[0]
        list_c[0] = c
        list_c.append(0)
    elif len(tuple_a) == 1:
        list_c.append(tuple_b[1])
    elif len(tuple_b) == 1:
        list_c.append(tuple_a[1])
    if len(tuple_b) == 0 and len(tuple_a) == 0:
        list_c.append(0)
        list_c.append(0)
    elif len(tuple_b) == 0:
        list_c.append(tuple_a[0])
        list_c.append(tuple_a[1])
    elif len(tuple_a) == 0:
        list_c.append(tuple_b[0])
        list_c.append(tuple_b[1])

    list_c = list_c[:2]
    tuple_c = tuple(list_c)
    return tuple_c
