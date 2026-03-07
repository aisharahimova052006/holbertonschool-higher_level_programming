#!/usr/bin/python3
"""we define custom object class"""
import pickle

class CustomObject:


    def __init__(self,name,age,is_student):
        self.name=name
        self.age=age
        self.is_student=is_student

    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Is Student: ",self.is_student)

    def serialize(self,filename):
        with open(filename,'wb') as f:
            pickle.dump(self,f)


    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename,'rb') as f:
                ClassObject=pickle.load(f)
        except EOFError:
            return None
        return ClassObject
