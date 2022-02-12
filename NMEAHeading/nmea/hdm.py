# HDM - Heading - Magnetic
# Vessel heading in degrees with respect to magnetic north produced by any device or system producing magnetic heading.
# $--HDM,x.x,M*hh<CR><LF>
# Heading Degrees, magnetic
# M = magnetic
# Checksum

class hdm():
    # Constructor
    def __init__(self):
        # Switch this on for verbose processing
        self.debug = 1

    @staticmethod
    def parse(sentence):
        # Default, invalid fix
        fix_quality = '0'
        gps_time = ''
        dd_longitude_degrees = 0
        dd_latitude_degrees = 0
        altitude3 = 0

    @staticmethod
    def create(sentence):
        # Default, invalid fix
        fix_quality = '0'
        gps_time = ''
        dd_longitude_degrees = 0
        dd_latitude_degrees = 0
        altitude3 = 0