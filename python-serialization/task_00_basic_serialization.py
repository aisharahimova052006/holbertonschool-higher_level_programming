#!/usr/bin/python3
"""we define serialize and deserialize functions"""
import pickle


def serialize_and_save_to_file(data,filename):
    try:
        with open(filename,"wb") as file:
            pickle.dump(data,file)
    except AttributeError:
        raise TypeError

def load_and_deserialize(filename):
    with open (filename,"rb") as file:
        new_data=pickle.load(file)
        return new_data
