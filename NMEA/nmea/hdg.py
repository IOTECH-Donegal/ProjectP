# HDG - Heading - Deviation & Variation
# $--HDG,x.x,x.x,a,x.x,a*hh<CR><LF>
# Magnetic Sensor heading in degrees
# Magnetic Deviation, degrees
# Magnetic Deviation direction, E = Easterly, W = Westerly
# Magnetic Variation degrees
# Magnetic Variation direction, E = Easterly, W = Westerly
# Checksum

class hdg():
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