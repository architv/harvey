import re
import json

from bs4 import BeautifulSoup
import requests

RESOURCES = {}
BASE_URL = "https://api.github.com"
_HEADERS = {'Accept': 'application/vnd.github.drax-preview+json'}

with open('licences_tldr.json', 'r') as f:
  RESOURCES = json.loads(f.read())


def get_summary(content):
  """Gets the summary of a license from tldrlegal.com"""
  soup = BeautifulSoup(content, "html.parser")
  summary = soup.find_all(attrs={
      'class': re.compile(r".*\bsummary-content\b.*")})

  if summary[0].p.string is None:
    return summary[0].p.p.getText()
  return summary[0].p.getText()


def get_rules(license):
  """Gets can, cannot and must rules from github license API"""

  can = []
  cannot = []
  must = []
  req = requests.get("{base_url}/licenses/{license}".format(
                     base_url=BASE_URL, license=license), headers=_HEADERS)

  if req.status_code == requests.codes.ok:
    data = req.json()
    can = data["permitted"]
    cannot = data["forbidden"]
    must = data["required"]

  return can, cannot, must


def main():
  """Gets all the license information and stores it in json format"""

  all_summary = {}

  for license in RESOURCES:

    req = requests.get(RESOURCES[license])

    if req.status_code == requests.codes.ok:
      summary = get_summary(req.text)
      can, cannot, must = get_rules(license)

      all_summary[license] = {
          "summary": summary,
          "source": RESOURCES[license],
          "can": can,
          "cannot": cannot,
          "must": must
      }

  with open('summary.json', 'w+') as f:
    f.write(json.dumps(all_summary, indent=4))


if __name__ == '__main__':
  main()
