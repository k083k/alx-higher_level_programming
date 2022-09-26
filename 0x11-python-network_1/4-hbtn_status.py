#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status using requests"""
from requests import get

if __name__ == "__main__":
    response = get("https://intranet.hbtn.io/status").text
    print("Body response:")
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))
