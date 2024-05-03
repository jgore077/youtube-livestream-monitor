# bin/bash
pip3 install -r ./requirements.txt
wget https://github.com/Kethsar/ytarchive/releases/download/v0.4.0/ytarchive_linux_amd64.zip
sudo apt install unzip -y
unzip ytarchive_linux_amd64.zip
rm ytarchive_linux_amd64.zip