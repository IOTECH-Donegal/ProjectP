'''
Multicast->Serial Server by: JOR
Reads multicast packets from a particular set of addresses and ports.
Test with McSimulator
Alpha: 08MAR22
'''
import socket, serial
import settings.mc as settings

# Set multicast information
MCAST_GRP = settings.MCSERVER["MCAST_GROUP"]
SERVER_ADDRESS1 = ('', settings.MCSERVER["PORT1"])
#SERVER_ADDRESS2 = ('', settings.MCSERVER["PORT2"])
SERVER_ADDRESS3 = ('', settings.MCSERVER["PORT3"])
MCAST_IF_IP = settings.MCSERVER["IP_ADDRESS"]
SERIALPORT = settings.MCSERVER["SERIALPORT"]

print('This is the server.')
print(f'Make sure its IP address matches {MCAST_IF_IP} in settings.')
print(f'This selects which interface is used to listen for multicast as {MCAST_GRP}.')
print('This script has no error handling, by design.')

s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s1.bind(SERVER_ADDRESS1)
print(f'Listening on {settings.MCSERVER["PORT1"]}')

#s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#s2.bind(SERVER_ADDRESS2)
#print(f'Listening on {settings.MCSERVER["PORT2"]}')

s3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s3.bind(SERVER_ADDRESS3)
print(f'Listening on {settings.MCSERVER["PORT3"]}')

# inet_aton converts IPv4 from the a dotted decimal string to 32 bit packed binary format
s1.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, socket.inet_aton(MCAST_GRP) + socket.inet_aton(MCAST_IF_IP))
#s2.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, socket.inet_aton(MCAST_GRP) + socket.inet_aton(MCAST_IF_IP))
s3.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, socket.inet_aton(MCAST_GRP) + socket.inet_aton(MCAST_IF_IP))


with serial.Serial(SERIALPORT) as s:
    s.baudrate = 115200
    s.bytesize = serial.EIGHTBITS
    s.parity = serial.PARITY_NONE
    s.stopbits = serial.STOPBITS_ONE
    s.timeout = None

    while True:
        print('Waiting to transceive messages')
        data1, address1 = s1.recvfrom(1024)
        print(f'received {len(data1)} bytes from s1 {address1} as {data1}')
        s.write(data1 + b'\r\n')

        data2, address2 = s2.recvfrom(1024)
        print(f'received {len(data2)} bytes from s2 {address2} as {data2}')
        s.write(data2 + b'\r\n')

        data3, address3 = s3.recvfrom(1024)
        print(f'received {len(data3)} bytes from s3 {address3}  as {data3}')
        s.write(data3 + b'\r\n')
