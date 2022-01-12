#!/usr/bin/python3
""" This is a Python script that takes your GitHub credentials
and uses the GitHub API to display your id"""

import requests
import sys

if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        owner_name, repository_name)

    request = requests.get(url)
    request_json = request.json()

    for i, count in enumerate(request_json):
        if i == 10:
            break

        print('{}: {}'.format(count.get('sha'), count.get(
            'commit').get('author').get('name')))
