#!/usr/bin/python3
"""takes a repository name and an owner name and
lists 10 commits (from the most recent to oldest)"""
from sys import argv
from requests import get

if __name__ == "__main__":
    url = "https://api.github.com/repos"
    owner = argv[2]
    repo = argv[1]
    url = url + "/" + owner + "/" + repo + "/commits"
    limit = {"per_page": 10}
    response = get(url, params=limit)
    for commit in response.json():
        sha = commit.get("sha")
        author = commit.get("commit").get("author").get("name")
        print("{}: {}".format(sha, author))
