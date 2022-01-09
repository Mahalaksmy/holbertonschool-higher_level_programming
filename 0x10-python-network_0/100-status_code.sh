#!/bin/bash
# This is a Script bash that sends a request to a URL passed as an argument, and displays only the status code
curl -sL "$1" -o /dev/null -w "%{http_code}" -I
