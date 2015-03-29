# BGP Atlas Monitor

The BGP Atlas Monitor (BAM) was developed during the RIPE Atlas Hackathon 2015
in Amsterdam. BAM goals are to display, in real time, informations that are
useful for network operators such as prefixes visibility as seen from RIS, or
ping delays as seen fron the RIPE Atlas probes.

Currently, you can provide an AS number to BAM. It will retrieve your IPv4 and
IPv6 prefixes from RIPE stat, and display their visibilities from RIS. It also
shows a map of the probes in your network, as well as a map displaying prefixes
visibility from the RIS collectors.

Command line tools are also available in order to manipulating ASes information.

The BAM team
  Guillaume Valadon
  Francois Contant
  Mathias Handsche
  Thomas Holterbach


## Screenshots

![BAM index page](https://raw.githubusercontent.com/guedou/bam/master/data/screenshots/bam_index.png)
![BAM collectors map](https://raw.githubusercontent.com/guedou/bam/master/data/screenshots/bam_maps_collectors.png)
![BAM probes map](https://raw.githubusercontent.com/guedou/bam/master/data/screenshots/bam_maps_probes.png)


## Try it yourself 

BAM is packaged to be easily tested using vagrant. On your host, you will only
need to install vagrant, ansible and virtualbox.

On Debian, you can install these packages using the following command line:
host# apt-get install ansible virtualbox vagrant

Use the following commands to prepare a BAM installation:

host $ vagrant up

host $ vagrant ssh -- -L 2807:localhost:5000

guest$ python bam.py YOUR_ASN

The -r flag could be used to generate random data and trigger BAM
visualisations.

Open a browser on your vagrant host to http://localhost:2807

Standalone maps are available at http://localhost:2807/map/collectors and
http://localhost:2807/map/probes

## Command line tools

### List the announced prefixes
$ python lib/tools/get_announced_prefixes.py 202214

### Display an ASN visibility
$ python lib/tools/get_visibility.py 202214

### Display a prefix visibility
$ python lib/tools/get_visibility_prefix.py 185.50.64.0/22

### List probes of an AS
$ python lib/tools/get_probes.py 202214

### List a prefix route objetcs
$ python lib/tools/get_route_objects.py 185.50.64.0/22
