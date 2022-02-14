# ProjectP
Repo for code for a moving base/rover, RTK position and heading sensor.
This was tested using Ardusimple ZED-9P based boards.
The configuration of these boards is stored under the directory UBXZED9P.

### Testing the code
The code here is a combination of functions from several different projects. 
Unit testing is done in the original repos where this code was extracted from.
For the moment, I have no plans to add unit tests here.

As an integration test, the data from the three sources was read by a PC using OpenCPN 5.6.
 
## NMEA
The NMEA code in this project is based on IOTECH/NMEA.
There are two executables, one for the 
- Base on multicast port 239.1.1.1:5001
- Heading sensor on multicast port 239.1.1.1:5002
They output of different multicast ports, so they can both work simultaneously.

## UBX
The UBlox code in this project is based on IOTECH/UBX.
Its output is to another multicast port 239.1.1.1:5003

## RTKLIB
This project also uses a compiled version of str2str from RTKLIB.
This provides RTCM from a CORS station.



