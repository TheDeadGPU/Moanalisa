#!/bin/bash

# Variables
INSTALLDIRECTORY="/home/pi/bootscripts"
SERVICE_CONTENTS="[Unit]
Description=Moanalisa Moan Service
[Service]
Type=simple
TimeoutStartSec=0
WorkingDirectory=$INSTALLDIRECTORY
ExecStart=/usr/bin/python $INSTALLDIRECTORY/moanalisa.py

[Install]
WantedBy=default.target"

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
echo "$SERVICE_CONTENTS" > /home/pi/.local/share/systemd/user/Moanalisa.service
chmod 644 /home/pi/.local/share/systemd/user/Moanalisa.service
systemctl --user enable /home/pi/.local/share/systemd/user/Moanalisa.service
systemctl --user start Moanalisa.service
systemctl --user status Moanalisa.service
echo "Moanalisa Service Installed!"