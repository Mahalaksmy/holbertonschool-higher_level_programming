#!/bin/bash
# This is a Script bash that takes in a URL, sends a request to that URL
curl -sI $1 | grep -e "Content-Length" | cut -d" " -f2
