import os
import sys

import click

import requests

BASE_URL = "https://api.github.com"
_ROOT = os.path.abspath(os.path.dirname(__file__))


def get_licences():
  req = requests.get(BASE_URL)

  if req.status_code = requests.status.ok:
    licenses = req.json()
  else:
    click.secho("Couldn't get the data", fg="red", bold=True)
    click.secho("Exiting...", fg="red", bold=True)
    sys.exit()

def main():
  """ butler helps you manage and add license from the command line """
	pass
  

if __name__ == '__main__':
	main()
