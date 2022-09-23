#!/usr/bin/python3
"""takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""
from sys import argv
from requests import auth, get

if __name__ == "__main__":
    url = "https://api.github.com/user"
    github_auth = auth.HTTPBasicAuth(argv[1], argv[2])
    json_response = get(url, auth=github_auth)
    print(json_response.json().get("id"))
