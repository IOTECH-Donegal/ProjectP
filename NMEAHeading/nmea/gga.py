from nmea.nmea_data import GGA_Quality

'''
GNGGA,120113.00,5510.0019168,N,00726.0946454,W,4,12,0.60,109.635,M,53.911,M,1.0,0000*73
1 - Fix taken at in UTC as hhmmss.ss
2 - Latitude (Northing) in DM
3 - NS Hemisphere
4 - Longitude (Easting) in DM
5 - EW Hemisphere
6 - Fix quality, see GGA_Quality
7 - Number of satellites being tracked
8 - Horizontal dilution of position (HDOP)
9 - Altitude, Metres, above mean sea level
10 - Altitude Unit
11 - Separation of geoid between mean sea level and WGS84 ellipsoid()
12 - Separation Unit
13 - Time in seconds since last DGPS update, SC104
14 - DGPS station ID number
'''


class gga():
    # Constructor
    def __init__(self):
        # Switch this on for verbose processing
        self.debug = 1

        self.date = ''
        self.time = ''
        self.debug = 1
        self.fix_quality = ''
        self.latitude = 0
        self.longitude = 0
        self.altitude = 0
        self.geoid_separation = 0
        self.sog = 0
        self.cmg = 0

    def parse(self, sentence):
        try:
            list_of_values = sentence.split(',')

            # Verify the quality of the solution
            number_satellites_tracked = list_of_values[7]
            fix_quality = list_of_values[6]

            # Check if valid sentence
            if int(list_of_values[6]) > 0:

                # Get latitude in DD rounded to 8 decimals
                self.latitude = round(float(list_of_values[2][:2]) + float(list_of_values[2][2:]) / 60, 8)
                if list_of_values[3] == 'S':
                    self.latitude = -self.latitude
                # Get longitude DD rounded to 8 decimals
                self.longitude = round(float(list_of_values[4][:3]) + float(list_of_values[4][3:]) / 60, 8)
                if list_of_values[5] == 'W':
                    self.longitude = -self.longitude
                # Get Altitude
                altitude = float(list_of_values[9])
                geoid_separation = float(list_of_values[11])
                # To get the true altitude, add height above MSL to HoG and then convert to OSGM15 externally, limit to 3 decimal places (mm)
                self.altitude = round(altitude + geoid_separation, 3)
                # Get time
                hour, minute, second = int(list_of_values[1][:2]), int(list_of_values[1][2:4]), int(list_of_values[1][4:6])
                self.time = (f'{hour}:{minute}:{second}')

                # Look up the Fix Quality
                if list_of_values[6] in GGA_Quality:
                    self.fix_quality = int(list_of_values[6])
                else:
                    self.fix_quality = ''

        except ValueError:
            print(f'[GGA] Error parsing {sentence}')

        return self.time, self.longitude, self.latitude, self.altitude, self.fix_quality

    @staticmethod
    def create(sentence):
        # Default, invalid fix
        fix_quality = '0'
        gps_time = ''
        dd_longitude_degrees = 0
        dd_latitude_degrees = 0
        altitude3 = 0