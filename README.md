# BGP Atlas Monitor

Hello RIPE Atlas Hackathon !

## Launch the server

host $ vagrant up

host $ vagrant ssh -- -L 2807:localhost:5000

guest$ cd /vagrant
guest$ python bam.py YOUR_ASN

Open Browser on Vagrant Host System to http://localhost:2807


## Command line tools

### List the announced prefixes
$ python lib/tools/get_announced_prefixes.py 202214

### Display an ASN visibility
$ python lib/tools/get_visiiblity.py 202214

### List probes of an AS
$ python lib/tools/get_probes.py 202214
