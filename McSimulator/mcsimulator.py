'''
Multicast client by: JOR
Sends multicast packets to a particular address and port.
Alpha: 13FEB22
08MAR22: Modified to send UDP packets to three separate ports, for testing
'''

import socket
import time
from datetime import datetime
import settings.mc as settings

# Set multicast information
MCAST_GRP = settings.MCCLIENT["MCAST_GROUP"]
MCAST_PORT1 = settings.MCCLIENT["PORT1"]
MCAST_PORT2 = settings.MCCLIENT["PORT2"]
MCAST_PORT3 = settings.MCCLIENT["PORT3"]
MCAST_IF_IP = settings.MCCLIENT["IP_ADDRESS"]

print(f'This is the client, make sure its IP address matches {MCAST_IF_IP} in settings.')
print(f'This selects which interface is used for multicast to {MCAST_GRP}.')
print('This script has no error handling, by design')

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) as s:
        # inet_aton converts IPv4 from the a dotted decimal string to 32 bit packed binary format
        s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, socket.inet_aton(MCAST_GRP) + socket.inet_aton(MCAST_IF_IP))
        message_text = "$GNGGA,120113.00,5510.0019168,N,00726.0946454,W,4,12,0.60,109.635,M,53.911,M,1.0,0000*73"
        #message_text = f"IOTECH {datetime.now()}"
        message = message_text.encode('utf-8')
        s.sendto(message, (MCAST_GRP, MCAST_PORT1))
        print(f'Sent {message_text} to {MCAST_GRP}:{MCAST_PORT1}')

        s.sendto(message, (MCAST_GRP, MCAST_PORT2))
        print(f'Sent {message_text} to {MCAST_GRP}:{MCAST_PORT2}')

        s.sendto(message, (MCAST_GRP, MCAST_PORT3))
        print(f'Sent {message_text} to {MCAST_GRP}:{MCAST_PORT3}')
        time.sleep(1)