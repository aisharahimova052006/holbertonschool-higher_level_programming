#!/usr/bin/python3
"""we define student class in module"""


class Student:

    """we define attributes and functions"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        dictionary = {}
        if not attrs:
            if attrs == []:
                return dictionary
            else:
                return self.__dict__
        else:
            length = len(attrs)
            i = 0
            while i < length:
                if attrs[i] in self.__dict__.keys():
                    dictionary[attrs[i]] = self.__dict__[attrs[i]]
                else:
                    pass
                i += 1
        return dictionary

    def reload_from_json(self, json):
        for key, value in json.items():
            self.__dict__[key] = json[key]
