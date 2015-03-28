# Retrieve the visibilty information

import requests, json

def get_visibility(asn):
  """Return a JSON document representing the visibility of an AS from each RIS collector."""

  URL = "https://stat.ripe.net/data/visibility/data.json?resource=%d" % asn
  try:
    data = requests.get(URL).content
    data = json.loads(data)
  except Exception, e:
    print e
    return None

  ret = []
  for rrc in data["data"]["visibilities"]:
      ipv4_full_table_peer_count = rrc["ipv4_full_table_peer_count"]
      ipv4_full_table_peers_not_seeing_count = len(rrc["ipv4_full_table_peers_not_seeing"])
      ipv6_full_table_peer_count = rrc["ipv6_full_table_peer_count"]
      ipv6_full_table_peers_not_seeing_count = len(rrc["ipv6_full_table_peers_not_seeing"])

      ipv4_peer_percentage  = ipv4_full_table_peer_count - ipv4_full_table_peers_not_seeing_count
      ipv4_peer_percentage /= (float(ipv4_full_table_peer_count))
      ipv6_peer_percentage  = ipv6_full_table_peer_count - ipv6_full_table_peers_not_seeing_count
      ipv6_peer_percentage /= (float(ipv6_full_table_peer_count))

      doc = {}
      doc["city"] = rrc["probe"]["city"]
      doc["name"] = rrc["probe"]["name"]
      doc["latitude"] = rrc["probe"]["latitude"]
      doc["longitude"] = rrc["probe"]["longitude"]
      doc["ipv4_peer_percentage"] = ipv4_peer_percentage
      doc["ipv6_peer_percentage"] = ipv6_peer_percentage
      doc["ipv6_peers_not_seeing"] = rrc["ipv6_full_table_peers_not_seeing"]
      doc["ipv4_peers_not_seeing"] = rrc["ipv4_full_table_peers_not_seeing"]

      ret += [ doc ]

  return ret


if __name__ == "__main__":
  import argparse, sys
  from prettytable import PrettyTable

  # Parse command line options
  parser = argparse.ArgumentParser("Display the visibility of an ASN")
  parser.add_argument("asn", type=int, help="The AS number that will be monitored")
  args = parser.parse_args()


  data = get_visibility(args.asn)
  if not data:
    print >> sys.stderr, "Can't retrieve data !"
    sys.exit(1)

  table = PrettyTable(["Collector", "IPv4 peers visibility %", "IPv6 peers visibility %"])
  for visibility in data:
    table.add_row([" - ".join([visibility["name"], visibility["city"]]), visibility["ipv4_peer_percentage"]*100, visibility["ipv6_peer_percentage"]*100])
  print table
 
