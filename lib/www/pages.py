import flask
import pandas as pd
from lib.tools.get_probes import *

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

  latitude = pd.Series(latitudes).mean()
  longitude = pd.Series(longitudes).mean()

  return flask.render_template("map_probes.html",
                               asn=asn,
                               latitude=latitude,
                               longitude=longitude,
                               probes=probes)
