#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status,
displays the value of X-Request-Id in the header using requests"""
from requests import get
from sys import argv
if __name__ == "__main__":
    response = get(argv[1]).headers
    print(response.get("X-Request-Id"))
