#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    empty_list = []
    for i in range(0, list_length):
        try:
            c = my_list_1[i]/my_list_2[i]
            empty_list.append(c)
        except ZeroDivisionError:
            print("division by 0")
            empty_list.append(0)
        except TypeError:
            print("wrong type")
            empty_list.append(0)
        except IndexError:
            print("out of range")
            empty_list.append(0)
        finally:
            pass
    return empty_list
