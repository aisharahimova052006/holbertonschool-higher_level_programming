#!/usr/bin/python3
"""get X-Request-Id header"""
import sys
import requests


if __name__ == "__main__":
    r = requests.get(sys.argv[1], headers={"cfclearance": "true"})
    print(r.headers.get("X-Request-Id"))
