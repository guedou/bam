import requests
import argparse
import json

def get_probes (asn):
    url = 'https://stat.ripe.net/data/atlas-probes/data.json?resource=AS'+str(asn)

    r = requests.get (url)

    data_json = json.loads(r.content)
	
    probes_list = []
    for probe in data_json["data"]["probes"]:
        if probe["status"] == 1:
            if 'address_v4' not in probe:
                probe['address_v4'] = 'Unknown'
            probes_list.append({'id':probe['id'], 'country_code':probe['country_code'], 'ipv4':probe['address_v4'], 'latitude':probe['latitude'], 'longitude':probe['longitude']})
        
    return probes_list


if __name__ == "__main__":

    from prettytable import PrettyTable

    parser = argparse.ArgumentParser("Get probes of an AS")
    parser.add_argument("asn", type=int, help="The AS number that will be monitored")
    args = parser.parse_args()

    probes_list = get_probes (args.asn)

    table = PrettyTable(["ID", "IPv4", "Country", "Latitude", "longitude"])
    for probe in probes_list:
        table.add_row([probe['id'], probe['ipv4'], probe['country_code'], probe['latitude'], probe['longitude']])
    print table
