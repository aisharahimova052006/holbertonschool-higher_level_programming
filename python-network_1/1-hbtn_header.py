#!/usr/bin/python3
"""
hhh
"""
from urllib import request
import sys
if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        headers = response.headers
        print(headers.get("X-Request-Id"))
