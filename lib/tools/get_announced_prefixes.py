import os
import mechanize
import json
import argparse

def get_announced_prefixes (asn):
	url = 'https://stat.ripe.net/data/announced-prefixes/data.json?resource=AS'+str(asn)

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

        v4_list = []
        v6_list = []
	for p in map(lambda x : x["prefix"], json_data["data"]["prefixes"]):
          if ":" in p:
            v6_list.append(p)
          else:
            v4_list.append(p)

	return { "v4": v4_list, "v6": v6_list }


if __name__ == "__main__":
    
	parser = argparse.ArgumentParser("Get Announced Prefixes")
	parser.add_argument("asn", type=int, help="The AS number that wil be monitored")
	args = parser.parse_args()

        prefixes = get_announced_prefixes(args.asn)
        for prefix in prefixes["v4"] + prefixes["v6"]:
          print prefix
