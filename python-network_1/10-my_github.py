#!/usr/bin/python3
# python script that takes your GitHub credentials (username and password),
# and uses the 'GitHub API' to display your 'id'
"""
    use 'GitHub API to display 'id'
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user/DUSHIME1212", auth=auth)
    print(r.json().get("id"))
