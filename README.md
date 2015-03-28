# BGP Atlas Monitor

Hello RIPE Atlas Hackathon !

## Launch the server

guest$ vagrant box add https://vagrantcloud.com/chef/boxes/debian-7.6

guest$ vagrant up

guest$ vagrant ssh -- -L 2807:localhost:5000

host $ python bam.py YOUR_ASN
