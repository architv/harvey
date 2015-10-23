import re

import json

from bs4 import BeautifulSoup
import requests

RESOURCES = {}

with open('licences_tldr.json', 'r') as f:
  RESOURCES = json.loads(f.read())


def get_summary(content):
  soup = BeautifulSoup(content, "html.parser")
  summary = soup.find_all(attrs={'class': re.compile(r".*\bsummary-content\b.*")})

  if summary[0].p.string == None:
    return summary[0].p.p.getText()
  return summary[0].p.getText()

def main():
  all_summary = {}

  for license in RESOURCES:

    req = requests.get(RESOURCES[license])

    if req.status_code == 200:
      summary = get_summary(req.text)
      all_summary[license] = {
        "summary": summary,
        "source": RESOURCES[license]
      }

  with open('summary.json', 'a') as f:
    f.write(json.dumps(all_summary, indent=4))


if __name__ == '__main__':
  main()


