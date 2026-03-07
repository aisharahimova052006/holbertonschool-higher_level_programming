#!/usr/bin/python3
"""Module contains the class which prints a list in sorted order."""


class MyList(list):

    """Class that extends list and adds a method to print it sorted."""

    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))

    def __str__(self):
        return "[" + ", ".join(str(x) for x in self) + "]"
