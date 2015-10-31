r"""
butler generates license  from the command line for you
Usage:
  butler (ls | list)
  butler [(-tldr NAME)]
  butler [NAME...]
  butler (-h | --help)
  butler --version
Options:
  -h --help     Show this screen.
  --version     Show version.
"""

import json
import os
import re
import sys

import requests
from docopt import docopt

__version__ = '0.0.1'

BASE_URL = "https://api.github.com"
_HEADERS = {'Accept': 'application/vnd.github.drax-preview+json'}
_LICENCES = {}

with open('licenses.json', 'r') as f:
  _LICENCES = json.loads(f.read())


def _get_licences():
  """ lists all the licenses on command line """
  licenses = {}
  with open('licenses.json', 'r') as f:
    licenses = json.loads(f.read())
  
    for license in licenses:
      print "{license_name} [{license_code}]".format(license_name=licenses[license], license_code=license)


def _get_license_description(license_code):
  """ Gets the body for a license based on a license code """
  req = requests.get("{base_url}/licenses/{license_code}".format(base_url=BASE_URL, 
    license_code=license_code), headers=_HEADERS)

  if req.status_code == requests.codes.ok:
    s = req.json()["body"]
    search_curly = re.search(r'\{(.*)\}', s)
    search_square = re.search(r'\[(.*)\]', s)
    matches = ""

    # if search_curly:
    #   matches = re.sub(r'\{(.+)\}', '2015 Archit Verma', s)
    # elif search_square:
    #   matches = re.sub(r'\[(.+)\]', '2015 Archit Verma', s)

    # return matches


    # print matches
  else:
    # click.secho("Couldn't get the data", fg="red", bold=True)
    # click.secho("Exiting...", fg="red", bold=True)
    sys.exit()


def get_license_summary(license_code):
  """ Gets the license summary and permitted, forbidden and required behavouir """
  with open('summary.json', 'r') as f:
    summary_license = json.loads(f.read())[license_code]
 

def main():
  ''' butler helps you manage and add license from the command line '''
	
  # for license in _LICENCES.keys():
  #   get_license_description(license)

  arguments = docopt(__doc__, version=__version__)

  if arguments['ls'] or arguments['list']:
    _get_licences()
  elif arguments['-tldr'] and arguments['NAME']:
    get_license_summary(arguments['NAME'])
  elif arguments['NAME']:
      print(_get_license_description(arguments['NAME']))
  else:
      print(__doc__)
  

if __name__ == '__main__':
	main()
