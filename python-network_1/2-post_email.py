#!/usr/bin/python3
"""send email with POST"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(email).encode("ascii")
    req = urllib.request.Request(url, data=data, headers={"cfclearance": "true"})
    with urllib.request.urlopen(req) as r:
        print(r.read().decode("utf-8"))
