#!/usr/bin/python3
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as r:
    x = r.info()
    print(x.get("X-Request-ID")
