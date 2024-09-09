#!/bin/bash

apt update
apt install -y ansible
sudo wget https://raw.githubusercontent.com/Bar-Tubul/Ansible_automation/main/playbook.yml -O /home/ubuntu/playbook.yml
ansible-playbook /home/ubuntu/playbook.yml
git clone https://github.com/Bar-Tubul/Ansible-CI-CD-FWS.git

