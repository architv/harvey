from bs4 import BeautifulSoup
import requests
import json

RESOURCES = {}

with open('licences_tldr.json', 'r') as f:
  RESOURCES = json.loads(f.read())


def get_summary():
  soup = BeautifulSoup(content)
  summary = soup.find_all(attrs={'class': re.compile(r".*\bquick-summary\b.*")})
  print summary


def create_json():

	for license in RESOURCES:
		req = requests.get(RESOURCES[license])

		if req.status_code == requests.status.ok:
			summary = get_summary(req.text)


create_json()


