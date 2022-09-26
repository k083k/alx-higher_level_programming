#!/usr/bin/python3
"""sends a POST request to argv[1] with email attached
and displays the result, using requests"""
from requests import post
from sys import argv

if __name__ == "__main__":
    payload = {"email": argv[2]}
    response = post(argv[1], data=payload).text
    print(response)
