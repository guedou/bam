import flask
import pandas as pd
from lib.tools.get_probes import *
from lib.tools.get_visibility import *

def map_probes(config, map_type="dynamic", radius=30000):
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

  if map_type == "dynamic":
    map_core = flask.render_template("map_dynamic.html",
                                 asn=asn,
                                 latitude=latitude,
                                 longitude=longitude,
                                 radius=radius,
                                 zoom=2,
                                 source="get_probes",
                                 api_key=config.get("GMAP_API_KEY", "DUMMY-KEY"))
  else:
    map_core = flask.render_template("map_static.html",
                                 asn=asn,
                                 latitude=latitude,
                                 longitude=longitude,
                                 markers=probes,
                                 radius=radius,
                                 zoom=2,
                                 api_key=config.get("GMAP_API_KEY", "DUMMY-KEY"))

  return flask.render_template("map_wrapper.html", map_core=map_core)


def map_collectors(config, map_type="dynamic", radius=150000):
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

  if map_type == "dynamic":
    map_core = flask.render_template("map_dynamic.html",
                                 asn=asn,
                                 latitude=latitude,
                                 longitude=longitude,
                                 radius=radius,
                                 zoom=2,
                                 source="get_visibility",
                                 api_key=config.get("GMAP_API_KEY", "DUMMY-KEY"))
  else:
    map_core = flask.render_template("map_static.html",
                                 asn=asn,
                                 latitude=latitude,
                                 longitude=longitude,
                                 markers=collectors,
                                 radius=radius,
                                 zoom=2,
                                 api_key=config.get("GMAP_API_KEY", "DUMMY-KEY"))

  return flask.render_template("map_wrapper.html", map_core=map_core)


def index(config):
  """Build the BAM index."""
  asn = config.get("asn", "No ASN provided !")

  rendered_map_probes = map_probes(config, "dynamic")
  #rendered_map_collectors = map_collectors(config, "dynamic")

  value = flask.render_template("index.html", asn=asn,
                                              map_probes=rendered_map_probes,
                                              map_collectors=rendered_map_collectors)

  return value
