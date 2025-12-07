#!/usr/bin/python3
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as r:
    x = r.getheader("X-Request-Id")
    if x is None:
        x = r.headers.get("X-Request-Id") or r.headers.get("x-request-id") or r.info().get("X-Request-Id")
    print(x)
