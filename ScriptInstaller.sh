#!/bin/bash

# Variables
INSTALLDIRECTORY="/bootscripts"
SERVICE_CONTENTS="[Unit]
Description=Moanalisa Moan Service
After=multi-user.target
User=pi

[Service]
Type=idle
ExecStart=/usr/bin/python $INSTALLDIRECTORY/moanalisa.py

[Install]
WantedBy=multi-user.target"

# Check to see if we are running as Root
if [ "$(id -u)" -ne 0 ]; then
    echo "This script must be run as root" >&2
    exit 1
fi

# Find the directory where the install script lives
BASEDIR=$(dirname "$0")
echo "Install Script is running from: $BASEDIR"

# Check to see if the bootscripts directory exists
if [ ! -d "$INSTALLDIRECTORY" ]; then
    mkdir -p "$INSTALLDIRECTORY"
    echo "Directory $INSTALLDIRECTORY created."
else
    echo "Directory $INSTALLDIRECTORY already exists."
fi

# Copy the moanalisa.py and dependencies scripts to the install location
cp "$BASEDIR/moanalisa.py" "$INSTALLDIRECTORY/moanalisa.py"
cp "$BASEDIR/Moaning.mp3" "$INSTALLDIRECTORY/Moaning.mp3"

# Create the Moanalisa Systemd Service
sudo echo "$SERVICE_CONTENTS" > /lib/systemd/system/Moanalisa.service
sudo chmod 644 /lib/systemd/system/Moanalisa.service
sudo systemctl daemon-reload
sudo systemctl enable Moanalisa
sudo service Moanalisa start
echo "Moanalisa Service Installed!"