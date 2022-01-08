#!/bin/bash
# This is a Script bash that takes in a URL and displays all HTTP methods the server will accept
curl -sX GET -H "X-HolbertonSchool-User-Id: 98" "$1"
