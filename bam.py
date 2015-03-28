# BGP Atlas Monitor

import argparse, os, json
import flask

import lib.www.pages
from lib.tools.get_announced_prefixes import *
from lib.tools.get_visibility import *


# The Flask application
app = flask.Flask(__name__,
                  template_folder="data/www/templates/",
                  static_folder="data/www/static/",
                  static_url_path="/static")

@app.route("/")
def flask_index():
  """BAM index"""

  return lib.www.pages.index(app.config["CONFIG"]["asn"])


@app.route("/get_prefixes")
@app.route("/get_prefixes/<int:asn>")
def flask_get_prefixes(asn=None):
  """Return the list of prefixes as seen by RIPE stat"""

  if asn == None:
    asn = app.config["CONFIG"]["asn"]

  doc = get_announced_prefixes(asn)
  doc["asn"] = asn

  return json.dumps(doc)


@app.route("/get_visibility")
@app.route("/get_visibility/<int:asn>")
def flask_get_visibility(asn=None):
  """Return the visibility as seen by RIPE stat."""

  if asn == None:
    asn = app.config["CONFIG"]["asn"]

  visibilities = get_visibility(asn)

  doc = {}
  doc["asn"] = asn
  doc["visibilities"] = visibilities

  return json.dumps(doc)


if __name__ == '__main__':

  # Parse command line options
  parser = argparse.ArgumentParser("BGP Atlas Monitor")
  parser.add_argument("-d", "--debug", dest="debug", action="store_true", default=False, help="Run in debug mode")
  parser.add_argument("asn", type=int, help="The AS number that will be monitored")
  args = parser.parse_args()

  # Global config
  config = {}
  config["asn"] = args.asn

  # Configure Flask
  app.config["CONFIG"] = config
  app.config["DEBUG"] = args.debug
  app.config["CSRF_ENABLED"] = True
  app.config["SECRET_KEY"] = os.urandom(128)

  # Start Flask
  app.run()
