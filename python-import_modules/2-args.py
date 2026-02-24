#!/usr/bin/python3
import sys
length = len(sys.argv)
if length - 1 == 0:
    print(f"{length-1} arguments.")
elif length - 1 == 1:
    print(f"{length-1} argument:")
else:
    print(f"{length-1} arguments:")
for i in range(1, length):
    b = sys.argv[i]
    str = "{}: {}".format(i, b)
    print(str)
if __name__ == "__main__":
    pass
