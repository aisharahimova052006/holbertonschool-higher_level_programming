#!/usr/bin/python3
"""get X-Request-Id header from url"""
import sys
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1], headers={"cfclearance": "true"})
    with urllib.request.urlopen(req) as r:
        print(r.headers.get("X-Request-Id"))
