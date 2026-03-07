#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    my_list = []
    my_list.append(length)
    if sentence:
        my_list.append(sentence[0])
    else:
        my_list.append(None)
    return my_list
