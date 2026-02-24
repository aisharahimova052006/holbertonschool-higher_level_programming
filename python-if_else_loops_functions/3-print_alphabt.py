#!/usr/bin/python3
print("".join(c for c in map(chr, range(97,123)) if c not in "eq"), end="")
