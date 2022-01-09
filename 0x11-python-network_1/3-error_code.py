#!/usr/bin/python3
""" This is a Python script that takes in a
URL and an email, sends a POST."""

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            html = response.read()
        print(html.decode("utf-8"))
    except urllib.error.HTTPError as type_error:
        print("Error code: {}".format(type_error.code))
