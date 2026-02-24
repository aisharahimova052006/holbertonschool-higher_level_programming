#!/usr/bin/python3
import sys
length = len(sys.argv)
integer = 0
for i in range(1, length):
    integer += int(sys.argv[i])
print(integer)
if __name__ == "__main__":
    pass
