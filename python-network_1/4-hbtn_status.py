#!/usr/bin/python3
"""fetch hbtn status"""
import requests


if __name__ == "__main__":
    r = requests.get("https://intranet.hbtn.io/status",
                     headers={"cfclearance": "true"})
    body = r.text
    print("Body response:")
    print("	- type:", type(body))
    print("	- content:", body)
