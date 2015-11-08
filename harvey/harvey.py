r"""

Harvey is a command line legal expert who manages license for you.

Usage:
  harvey (ls | list)
  harvey <NAME> --tldr
  harvey <NAME>
  harvey <NAME> --export
  harvey (-h | --help)
  harvey --version
Options:
  -h --help     Show this screen.
  --version     Show version.

"""


import json
import os
import re
import subprocess
import sys
from datetime import date

import requests
from colorama import Fore, Back, Style
from docopt import docopt

requests.packages.urllib3.disable_warnings()

__version__ = '0.0.5'

BASE_URL = "https://api.github.com"
_HEADERS = {'Accept': 'application/vnd.github.drax-preview+json'}
_LICENSES = {}
_ROOT = os.path.abspath(os.path.dirname(__file__))

filename = "licenses.json"
abs_file = os.path.join(_ROOT, filename)

with open(abs_file, 'r') as f:
  _LICENSES = json.loads(f.read())


def _stripslashes(s):
  '''Removes trailing and leading backslashes from string'''
  r = re.sub(r"\\(n|r)", "\n", s)
  r = re.sub(r"\\", "", r)
  return r


def _get_config_name():
  '''Get git config user name'''
  p = subprocess.Popen('git config --get user.name', shell=True,
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  output = p.stdout.readlines()
  return _stripslashes(output[0])


def _get_licences():
  """ Lists all the licenses on command line """
  licenses = _LICENSES

  for license in licenses:
    print("{license_name} [{license_code}]".format(
          license_name=licenses[license], license_code=license))


def _get_license_description(license_code):
  """ Gets the body for a license based on a license code """
  req = requests.get("{base_url}/licenses/{license_code}".format(
      base_url=BASE_URL, license_code=license_code), headers=_HEADERS)

  if req.status_code == requests.codes.ok:
    s = req.json()["body"]
    search_curly = re.search(r'\{(.*)\}', s)
    search_square = re.search(r'\[(.*)\]', s)
    license = ""
    replace_string = '{year} {name}'.format(year=date.today().year,
                                            name=_get_config_name())

    if search_curly:
      license = re.sub(r'\{(.+)\}', replace_string, s)
    elif search_square:
      license = re.sub(r'\[(.+)\]', replace_string, s)
    else:
      license = s

    return license
  else:
    print(Fore.RED + 'No such license. Please check again.'),
    print(Style.RESET_ALL),
    sys.exit()


def get_license_summary(license_code):
  """ Gets the license summary and permitted, forbidden and required
  behaviour """
  try:
    abs_file = os.path.join(_ROOT, "summary.json")
    with open(abs_file, 'r') as f:
      summary_license = json.loads(f.read())[license_code]

    # prints summary
    print(Fore.YELLOW + 'SUMMARY')
    print(Style.RESET_ALL),
    print(summary_license['summary'])

    # prints source for summary
    print(Style.BRIGHT + 'Source:'),
    print(Style.RESET_ALL),
    print(Fore.BLUE + summary_license['source'])
    print(Style.RESET_ALL)

    # prints cans
    print(Fore.GREEN + 'CAN')
    print(Style.RESET_ALL),
    for rule in summary_license['can']:
      print(rule)
    print('')

    # prints cannot
    print(Fore.RED + 'CANNOT')
    print(Style.RESET_ALL),
    for rule in summary_license['cannot']:
      print(rule)
    print('')

    # prints musts
    print(Fore.BLUE + 'MUST')
    print(Style.RESET_ALL),
    for rule in summary_license['must']:
      print(rule)
    print('')

  except KeyError:
    print(Fore.RED + 'No such license. Please check again.'),
    print(Style.RESET_ALL),


def save_license(license_code):
  """ Grab license, save to LICENSE/LICENSE.txt file """
  desc = _get_license_description(license_code)
  fname = "LICENSE"
  if sys.platform == "win32":
    fname += ".txt"  # Windows and file exts
  with open(os.path.join(os.getcwd(), fname), "w") as afile:
    afile.write(desc)


def main():
  ''' harvey helps you manage and add license from the command line '''
  arguments = docopt(__doc__, version=__version__)

  if arguments['ls'] or arguments['list']:
    _get_licences()
  elif arguments['--tldr'] and arguments['<NAME>']:
    get_license_summary(arguments['<NAME>'].lower())
  elif arguments['--export'] and arguments['<NAME>']:
    save_license(arguments['<NAME>'].lower())
  elif arguments['<NAME>']:
    print(_get_license_description(arguments['<NAME>'].lower()))
  else:
    print(__doc__)


if __name__ == '__main__':
  main()
