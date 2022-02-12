import serial
import sys
from nmea.utilities import udp_sender


# Utilities used for file handling and logging
from utilities.file import log_file_name as log_file_name

# NMEA Log File
nmea_log_file_name = './logfiles/' + log_file_name('.nmea')
# Open the file for append
nmea_output_file = open(nmea_log_file_name, 'a', newline='')

# Set UDP multicast information
MCAST_GRP = '224.1.1.1'
MCAST_PORT = 5002

print('***** NMEA Heading Sensor *****')
print('Accepts NMEA from a serial port:')
print('1. Extracts information and logs raw NMEA')
print('2. Outputs to a multicast address 224.1.1.1:5002 for other applications to use.')

try:
    with serial.Serial("/dev/ttyAMA3") as serial_port:
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
                    nmea_output_file.writelines(nmea_full_string)
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
