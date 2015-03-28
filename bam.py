# BGP Atlas Monitor

import argparse, os, json
import flask

import lib.www.pages


# The Flask application
app = flask.Flask(__name__,
                  template_folder="data/www/templates/",
                  static_folder="data/www/static/",
                  static_url_path="/static")

@app.route("/")
def index():
  """BAM index"""

  return lib.www.pages.index(app.config["CONFIG"])


@app.route("/get_prefixes")
def get_prefixes():
  """Get the list of prefixes"""

  return json.dumps(["192.168.0/24", "172.16.28.0/24"])


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
