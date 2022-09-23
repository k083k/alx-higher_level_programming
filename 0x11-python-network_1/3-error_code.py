#!/usr/bin/python3
"""takes in a URL, sends a request to the URL
and displays the response, handles exceptions"""
from urllib import request, error
from sys import argv

if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode(encoding='utf-8'))
    except error.HTTPError as http_err:
        print("Error code: {}".format(http_err.code))
