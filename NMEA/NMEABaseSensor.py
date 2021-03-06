import serial
import sys

# Utilities for any NMEA script
from nmea.utilities import mc_sender, ip_validator, udp_sender
from utilities.file import log_file_name as log_file_name

# Get all the settings for this programme
import settings.sensors as settings

this_programme = settings.NMEABASESENSOR['PROG']
MCAST_GRP = settings.NMEABASESENSOR["MCAST_GROUP"]
MCAST_PORT = settings.NMEABASESENSOR["MCAST_PORT"]
SERIAL_DEVICE = settings.NMEABASESENSOR["SERIAL_DEVICE"]
#MY_IPv4_ADDRESS = settings.NMEABASESENSOR["MY_IPv4_ADDRESS"]
#ip_validator(MY_IPv4_ADDRESS)

# NMEA Log File
nmea_log_file_name = './base/' + log_file_name('.nmea')
# Open the file for append
nmea_output_file = open(nmea_log_file_name, 'a', newline='')

print(f'***** {this_programme} *****')
print(f'Accepts NMEA from serial port {SERIAL_DEVICE}')
print('1. Extracts information and logs raw NMEA')
print(f'2. Outputs to a multicast address {MCAST_GRP}:{MCAST_PORT} for other applications to use.')
print(f'Logging as {nmea_output_file}')

try:
    with serial.Serial(SERIAL_DEVICE) as serial_port:
        serial_port.baudrate = 115200
        serial_port.bytesize = serial.EIGHTBITS
        serial_port.parity = serial.PARITY_NONE
        serial_port.stopbits = serial.STOPBITS_ONE
        serial_port.timeout = None

        while True:
            # Read the first byte, if no byte, loop
            byte1 = serial_port.read(1)
            if len(byte1) < 1:
                break

            # Check for NMEA0183, leading with a $ symbol
            elif byte1 == b"\x24":
                nmea_full_bytes = serial_port.readline()
                nmea_full_string = nmea_full_bytes.decode("latin-1")
                # Check for corrupted lines
                if nmea_full_string.isascii():
                    # Log NMEA text string
                    nmea_output_file.writelines(nmea_full_string)
                    # Send a multicast of the GGA sentence only
                    list_of_values = nmea_full_string.split(',')
                    sentence_id = list_of_values[0][2:]
                    if sentence_id == 'GGA':
                        # Use mc_sender for a specific interface
                        #mc_sender(MY_IPv4_ADDRESS, MCAST_GRP, MCAST_PORT, b"\x24" + nmea_full_bytes)
                        udp_sender(MCAST_GRP, MCAST_PORT, b"\x24" + nmea_full_bytes)
                    # Force OS to write each line, not to buffer
                    nmea_output_file.flush()
                    print(f'NMEA: Received {nmea_full_string.strip()}')

except serial.SerialException as err:
    print(f"Terminating with a serial port error: \n {err}")
    sys.exit()
except ValueError as err:
    print(f"Value Error error: {err}")
except OSError as err:
    print(f"OS error: {err}")
except Exception as err:
    print(f"Terminating with an unclassified error: \n {err}")
    sys.exit()
except KeyboardInterrupt:
    print('User has terminated the programme via the keyboard')
    nmea_output_file.close()
    sys.exit()
