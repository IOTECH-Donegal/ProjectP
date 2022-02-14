#!/bin/bash
# by: JOR
# Date: 12FEB22
# Function: Gets NTRIP from remote and forwards to local serial port, also acts as an RTCM TCP server
# Leave this script in /home/pi
# Script: str2str.sh

HOMEPATH="/home/pi"

# Configure hardware serial port
stty -F /dev/ttyAMA1 clocal raw speed 115200

# Get RTCM3 from RTK2GO and send to Ardusimple
$HOMEPATH/rtklib/str2str/str2str -in ntripcli://:@rtk2go.com/Umricam -out serial://ttyAMA1:115200:8:n:1 -out tcpsvr://:12345
