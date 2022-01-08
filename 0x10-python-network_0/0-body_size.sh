#!/bin/bash
# This is a Script bash that takes in a URL, sends a request to that URL
curl -s "$1"| grep -e "Content-Length" | wc -c