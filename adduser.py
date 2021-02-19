# How to run script
# python .\adduser.py personal_access_token_from_github github_username

import sys
import requests


def main():
    adduser(t, username)


def adduser(t, username):
    # Authenticate to GitHub

    headers = {
        "authorization": 'token ' + t
    }

    url = f"https://api.github.com/repos/CloudSkills/posts/collaborators/{username}"

    print(requests.put(url, headers=headers))


t = sys.argv[1]
username = sys.argv[2]

main()
