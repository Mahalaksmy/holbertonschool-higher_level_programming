#!/usr/bin/python3
""" This is a Python script that takes in a
URL and an email, sends a POST."""

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    data = urllib.parse.urlencode({"email": sys.argv[2]}).encode("ascii")
    with urllib.request.urlopen(sys.argv[1], data) as response:
        html = response.read()
        print(html.decode("UTF-8"))
