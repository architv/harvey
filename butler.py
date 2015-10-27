import os
import sys

import requests

BASE_URL = "https://api.github.com"
_HEADERS = {'Accept': 'application/vnd.github.drax-preview+json'}


def get_licences():
  req = requests.get(BASE_URL, headers=_HEADERS)

  if req.status_code == requests.codes.ok:
    return req.json()
  else:
    click.secho("Couldn't get the data", fg="red", bold=True)
    click.secho("Exiting...", fg="red", bold=True)
    sys.exit()


def _get_licences():
  """ lists all the licenses on command line """
  licenses = {}
  with open('licenses.json', 'r') as f:
    licenses = json.loads(f.read())
  
    for license in licenses:
      print "{license_name} [{license_code}]".format(license_name=licenses[license], license_code=license)


def get_license_description(license_code):
  """ Gets the body for a license based on a license code """
  req = requests.get("{base_url}/licenses/{license_code}".format(base_url=BASE_URL, 
    license_code=license_code), headers=_HEADERS)

  if req.status_code == requests.codes.ok:
    print req.json()["body"]
  else:
    # click.secho("Couldn't get the data", fg="red", bold=True)
    # click.secho("Exiting...", fg="red", bold=True)
    sys.exit()


def get_license_summary(license_code):
  """ Gets the license summary and permitted, forbidden and required behavouir """
  with open('summary.json', 'r') as f:
    summary_license = json.loads(f.read())[license_code]
 

def main():
  """ butler helps you manage and add license from the command line """
	# arguments = docopt(__doc__, version=__version__)

 #  if arguments['ls'] or arguments['list']:
 #      print(_get_filenames())
 #  elif arguments['NAME']:
 #      print(_handle_gitignores(arguments['NAME']))
 #  else:
 #      print(__doc__)
  get_license_description("apache-2.0")
  

if __name__ == '__main__':
	main()
