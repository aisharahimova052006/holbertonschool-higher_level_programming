#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        c = a/b
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: ", end='')
        if b != 0:
            print("{:.1f}".format(c))
        else:
            print(None)
    return c
