#!/usr/bin/python3
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as r:
    print(r.headers.get("X-Request-Id"))
