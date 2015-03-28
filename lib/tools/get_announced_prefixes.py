import os
import mechanize
import json
import argparse

def get_announced_prefixes (asn):
	url = 'https://stat.ripe.net/data/announced-prefixes/data.json?resource=AS'+str(asn)
	print url

	br = mechanize.Browser()

	try:
		data = br.open(url, timeout=10.0).read()
	except (mechanize.HTTPError,mechanize.URLError) as e:
		if isinstance(e, mechanize.HTTPError):
			print ('HTTPError '+str(e.code))
		else:
			print ('URLError '+e.reason)
		return []

	json_data = json.loads(data)

	prefixes_list = []
	for p in json_data["data"]["prefixes"]:
		prefixes_list.append(p["prefix"])

	print prefixes_list

if __name__ == "__main__":
    
	parser = argparse.ArgumentParser("Get Announced Prefixes")
	parser.add_argument("asn", type=int, help="The AS number that wil be monitored")
	args = parser.parse_args()

	get_announced_prefixes (args.asn)
