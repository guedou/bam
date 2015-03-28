# BGP Atlas Monitor

Hello RIPE Atlas Hackathon !

## Launch the server

host $ vagrant up

host $ vagrant ssh -- -L 2807:localhost:5000

guest$ cd /vagrant
guest$ python bam.py YOUR_ASN

Open Browser on Vagrant Host System to http://localhost:2807
