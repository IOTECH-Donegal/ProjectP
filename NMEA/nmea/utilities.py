import socket


def mc_sender(mcast_if_ip, mcast_grp, mcast_port, message):
    this_function = 'mc_sender'
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        s.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_IF, socket.inet_aton(mcast_if_ip))
        s.sendto(message, (mcast_grp, mcast_port))
    except socket.error as e:
        print(f'Error {e} in nmea utilities, function {this_function}')
        exit(-1)

def ip_validator(IPv4):
    this_function = 'ip_validator'
    try:
        socket.inet_aton(IPv4)
    except socket.error:
        print(f'The IP address {IPv4} in the settings does not appear on this computer')
        exit(-1)


def udp_sender(MCAST_GRP, MCAST_PORT, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)
    sock.sendto(message, (MCAST_GRP, MCAST_PORT))


def validate_crc(nmea_full_sentence):
    """
    Compare a calculated CRC to the received value
    Assumes $ has been pre-stripped
    Assumes CR LF have been pre-stripped
    """

    try:
        # The last two characters are HH where HH is the CRC
        checksum = nmea_full_sentence[-2:]
        # XOR all values between $ and *
        calculated_checksum = calculate_crc(nmea_full_sentence[0:-3])
        # Compare the calculated checksum with the numerical value of the extracted string, upper case
        if calculated_checksum == checksum.upper():
            return True
        else:
            return False
    except:
        print('Error trying to validate CRC in ' + nmea_full_sentence)


def calculate_crc(nmea_partial_sentence):
    """
    Calculate the CRC of a NMEA sentence, CRC is a simple XOR of all values between $ and *
    """

    # Reset to zero
    calculated_checksum = 0
    # Go through each character and XOR, create an integer
    for character in nmea_partial_sentence:
        calculated_checksum ^= ord(character)
    # Convert to hex, 2 digits
    calculated_checksum_2_digits = format(calculated_checksum, '02X')
    return calculated_checksum_2_digits


def time_difference(dt1, dt2):
    dt = dt2 - dt1
    return dt.total_seconds()