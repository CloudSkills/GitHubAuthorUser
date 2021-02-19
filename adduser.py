# How to run script
# python .\adduser.py personal_access_token_from_github github_username

import sys
import requests
import logging


def main():
    try:
        adduser(t, username)
    
    except Exception as e:
        logging.error(e)


def adduser(t, username):
    # Authenticate to GitHub

    headers = {
        "authorization": 'token ' + t
    }

    url = f"https://api.github.com/repos/CloudSkills/posts/collaborators/{username}"

    try:
        print(requests.put(url, headers=headers))
        print('GitHub User Added ')
    
    except Exception as e:
        logging.error(e)


t = sys.argv[1]
username = sys.argv[2]

main()
