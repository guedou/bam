# Retrieve the visibilty information

import requests, json, random

def get_visibility_prefix(prefix, random_data=False):
  """Return a JSON document representing the visibility of a prefix from each RIS collector."""

  URL = "https://stat.ripe.net/data/visibility/data.json?resource=%s" % prefix
  try:
    data = requests.get(URL).content
    data = json.loads(data)
  except Exception, e:
    print e
    return None

  if data["status"] == "error":
    return None

  addr_type = "v4"
  if ":" in prefix:
    addr_type = "v6"

  # Automatically adjust the size of the returned list
  collectors = [element["probe"]["name"] for element in data["data"]["visibilities"]]
  collectors_int = [int(name[3:]) for name in collectors]
  ret = [None] * (max(collectors_int)+1)

  for rrc in data["data"]["visibilities"]:
      full_table_peer_count = rrc["ip%s_full_table_peer_count" % addr_type]
      full_table_peers_not_seeing_count = len(rrc["ip%s_full_table_peers_not_seeing" % addr_type])
      peer_percentage  = full_table_peer_count - full_table_peers_not_seeing_count
      peer_percentage /= (float(full_table_peer_count))

      doc = {}
      doc["city"] = rrc["probe"]["city"]
      doc["name"] = rrc["probe"]["name"]
      doc["latitude"] = rrc["probe"]["latitude"]
      doc["longitude"] = rrc["probe"]["longitude"]
      doc["peer_percentage"] = peer_percentage
      doc["peers_not_seeing"] = rrc["ip%s_full_table_peers_not_seeing" % addr_type]

      if random_data:
        doc["peer_percentage"] = random.randint(1, 100) / 100.

      rrc_id = int(doc["name"][3:])

      ret[rrc_id] = doc

  return ret


if __name__ == "__main__":
  import argparse, sys
  from prettytable import PrettyTable

  # Parse command line options
  parser = argparse.ArgumentParser("Display the visibility of a prefix")
  parser.add_argument("prefix", help="The prefix that will be monitored")
  args = parser.parse_args()


  data = get_visibility_prefix(args.prefix)
  if not data:
    print >> sys.stderr, "Can't retrieve data !"
    sys.exit(1)

  table = PrettyTable(["Collector", "Peers visibility %"])
  for visibility in data:
    if not visibility:
      continue
    table.add_row([" - ".join([visibility["name"], visibility["city"]]), visibility["peer_percentage"]*100])
  print table
 
