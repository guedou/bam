# BGP Atlas Monitor

The BGP Atlas Monitor (BAM) was developped during the RIPE Atlas Hackathon 2015
in Amsterdam. BAM goals are to display, in real time, informations that are
useful for network operators such as prefixes visibility as seen from RIS, or
ping delays as seen fron the RIPE Atlas probes.

The BAM team
  Guillaume Valadon
  Francois Contant
  Mathias Handsche
  Thomas Holterbach


## Try it yourself 

BAM is packaged to be easily tested using vagrant. On your host, you will only
need to install vagrant, ansible and virtualbox.

On Debian, you can install these packages using the following command line:
host# apt-get install ansible virtualbox vagrant

Use the following commands to prepare a BAM installation:

host $ vagrant up

host $ vagrant ssh -- -L 2807:localhost:5000

guest$ python bam.py YOUR_ASN

Open a browser on your vagrant host to http://localhost:2807


## Command line tools

### List the announced prefixes
$ python lib/tools/get_announced_prefixes.py 202214

### Display an ASN visibility
$ python lib/tools/get_visibility.py 202214

### Display a prefix visibility
$ python lib/tools/get_visibility_prefix.py 185.50.64.0/22

### List probes of an AS
$ python lib/tools/get_probes.py 202214

### List an ASN route objetcs
$ python lib/tools/get_route_objects.py 185.50.64.0/22
