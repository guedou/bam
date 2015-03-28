import flask

def index(config):
  """Build the BAM index."""
  asn = config.get("asn", "No ASN provided !")

  return flask.render_template("index.html", asn=asn)
