import flask
import pandas as pd
from lib.tools.get_probes import *
from lib.tools.get_visibility import *

def index(config):
  """Build the BAM index."""
  asn = config.get("asn", "No ASN provided !")

  return flask.render_template("index.html", asn=asn)


def map_probes(config):
  """Build the probes map."""
  asn = config.get("asn", "No ASN provided !")

  probes = get_probes(asn)

  latitudes = []
  longitudes = []
  for probe in probes:
    latitudes.append(probe["latitude"])
    longitudes.append(probe["longitude"])
    probe["content"] = "Probe ID: %s" % probe["id"]
    #if probe.get("ipv4", None):
    #  probe["content"] += "IPv4: %s<br>" % probe["ipv4"]
    #if probe.get("ipv6", None):
    #  probe["content"] += "IPv6: %s<br>" % probe["ipv6"]

  latitude = pd.Series(latitudes).mean()
  longitude = pd.Series(longitudes).mean()

  return flask.render_template("map.html",
                               asn=asn,
                               latitude=latitude,
                               longitude=longitude,
                               markers=probes,
                               radius=30000,
                               zoom=5,
                               api_key=config.get("GMAP_API_KEY", "DUMMY-KEY"))


def map_collectors(config):
  """Build the collectors map."""
  asn = config.get("asn", "No ASN provided !")

  collectors = filter(lambda p: p != None, get_visibility(asn))

  latitudes = []
  longitudes = []
  for collector in collectors:
    if not collector:
      continue
    latitudes.append(collector["latitude"])
    longitudes.append(collector["longitude"])
    collector["content"] = "Collector: %s" % collector["name"]
    collector["id"] = collector["name"][3:]

  latitude = pd.Series(latitudes).mean()
  longitude = pd.Series(longitudes).mean()

  return flask.render_template("map.html",
                               asn=asn,
                               latitude=latitude,
                               longitude=longitude,
                               markers=collectors,
                               radius=150000,
                               zoom=2,
                               api_key=config.get("GMAP_API_KEY", "DUMMY-KEY"))
