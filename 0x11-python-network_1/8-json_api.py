#!/usr/bin/python3
""" This is a Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user"""


import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""

    else:
        q = sys.argv[1]

    request = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})

    try:
        value = request.json()
        if value == {}:
            print("No result")
        else:
            print("[{}] {}".format(value.get("id"), val.get("name")))
    except ValueError:
        print("Not a valid JSON")
