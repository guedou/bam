import requests
import argparse
import json
import random

def get_probes (asn, random_data=False):
    url = 'https://stat.ripe.net/data/atlas-probes/data.json?resource=AS'+str(asn)

    r = requests.get (url)

    try:
        data_json = json.loads(r.content)
    except ValueError:
        print 'get_probes.py : JSon unreadable'	

    probes_list = []
    for probe in data_json["data"]["probes"]:
        if probe["status"] == 1:
            if 'address_v4' not in probe:
                probe['address_v4'] = 'Unknown'
            if 'address_v6' not in probe:
                probe['address_v6'] = 'Unknown'

            if random_data:
              index = random.randint(0, 2)
              probe["color"] = ["#00FF00", "#FF0000", "#FFA500"][index]
            else:
              probe["color"] = "#00FF00"

            probes_list.append({'id':probe['id'], 'country_code':probe['country_code'], 'ipv4':probe['address_v4'], 'ipv6':probe['address_v6'], 'latitude':probe['latitude'], 'longitude':probe['longitude'], "color" : probe["color"]})


    return probes_list


if __name__ == "__main__":

    from prettytable import PrettyTable

    parser = argparse.ArgumentParser("Get probes of an AS")
    parser.add_argument("asn", type=int, help="The AS number that will be monitored")
    args = parser.parse_args()

    probes_list = get_probes (args.asn)

    table = PrettyTable(["ID", "IPv4", "IPv6", "Country", "Latitude", "longitude"])
    for probe in probes_list:
        table.add_row([probe['id'], probe['ipv4'], probe['ipv6'], probe['country_code'], probe['latitude'], probe['longitude']])
    print table
