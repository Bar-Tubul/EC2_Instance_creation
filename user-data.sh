#!/bin/bash

apt update
apt install -y ansible
sudo wget https://raw.githubusercontent.com/CapSuleFor/bar-playbook/main/playbook.yml -O /home/ubuntu/playbook.yml
ansible-playbook /home/ubuntu/playbook.yml
