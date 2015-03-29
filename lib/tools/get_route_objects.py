# Retrieve route objects from RIPE whois database

import requests, json, random

def get_route_objects(prefix, random_data=False):
  """Return a JSON document containing whois information about a prefix."""

  URL = "https://stat.ripe.net/data/whois/data.json?resource=%s" % prefix
  try:
    data = requests.get(URL).content
    data = json.loads(data)
  except Exception, e:
    print e
    return None

  ret = []
  for obj in data["data"]["irr_records"]:
    route_object = [None] * 2
    for tmp in obj:
      if tmp["key"] == "route":
        route_object[0] = tmp["value"]
      if tmp["key"] == "origin":
        route_object[1] = tmp["value"]
    if not None in route_object:
      ret.append((route_object[0], route_object[1]))

  return ret


if __name__ == "__main__":
  import argparse, sys
  from prettytable import PrettyTable

  # Parse command line options
  parser = argparse.ArgumentParser("Display route ojects")
  parser.add_argument("prefix",  help="The prefix number that will be monitored")
  args = parser.parse_args()


  data = get_route_objects(args.prefix)
  if not data:
    print >> sys.stderr, "Can't retrieve data !"
    sys.exit(1)


  table = PrettyTable(["ASN", "Prefix"])
  for ro, asn in data:
    table.add_row([asn, ro])
  print table
