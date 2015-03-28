# BGP Atlas Monitor

Hello RIPE Atlas Hackathon !

## Launch the server

guest$ vagrant up

guest$ vagrant ssh -- -L 2807:localhost:5000

host $ python bam.py YOUR_ASN

open Browser on Vagrant Host System to http://localhost:2807
