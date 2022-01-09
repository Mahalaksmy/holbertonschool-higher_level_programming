#!/bin/bash
# This is a Script bash that takes in a URL and displays all HTTP methods the server will accept
curl -s --head "$1" | grep Allow | cut --complement -d' ' -f1
