import datetime
from nmea.nmea_data import RMC_PosMode as PosMode

'''
RMC - Recommended minimum specific GPS/Transit data
GNRMC,120112.00,A,5510.0019172,N,00726.0946444,W,0.017,,070921,,,R,V*1E
1 - Fix taken at in UTC as hhmmss.ss
2 - Data validity, A=Valid, V=Invalid
2 - Latitude (Northing) in DM
3 - NS Hemisphere
4 - Longitude (Easting) in DM
5 - EW Hemisphere
7 - Speed over ground in Knots
8 - Course Made Good in Degrees, True
9 - Date of fix DDMMYY
10 - Magnetic variation
11 - Magnetic variation hemisphere
12 - posMode indicator (from NMEA 2.3 onwards)
13 - navStatus, fixed field (from NMEA 4.1 onwards), always V
'''

class rmc():
    # Constructor
    def __init__(self):
        # Switch this on for verbose processing
        self.date = ''
        self.time = ''
        self.debug = 1
        self.PosMode = ''
        self.latitude = 0
        self.longitude = 0
        self.sog = 0
        self.cmg = 0

    def parse(self, sentence):
        # Default, invalid fix
        data_validity = 'V'

        # Return values
        pos_mode_indicator = 'N'
        sog = '0'
        cmg = '0'
        date_of_fix = ''

        try:
            list_of_values = sentence.split(',')
            # Check if valid sentence
            if list_of_values[2] == 'A':
                # Get latitude in DD
                self.latitude = round(float(list_of_values[3][:2]) + float(list_of_values[3][2:]) / 60, 8)
                if list_of_values[4] == 'S':
                    self.latitude = -self.latitude
                # Get longitude DD
                self.longitude = round(float(list_of_values[5][:3]) + float(list_of_values[5][3:]) / 60, 8)
                if list_of_values[6] == 'W':
                    self.longitude = -self.longitude
                # Get date and time
                hour, minute, second = int(list_of_values[1][:2]), int(list_of_values[1][2:4]), int(list_of_values[1][4:6])
                day, month, year = int(list_of_values[9][:2]), int(list_of_values[9][2:4]), 2000 + int(list_of_values[9][4:])
                self.date = (f'{day}-{month}-{year}')
                self.time = (f'{hour}:{minute}:{second}')
                # Get speed and heading
                self.cmg = float(list_of_values[8]) if list_of_values[8] != "" else 0.0
                self.sog = float(list_of_values[7]) if list_of_values[7] != "" else 0.0

                # Look up the PosMode
                if list_of_values[12] in PosMode:
                    self.PosMode = list_of_values[12]
                else:
                    self.PosMode = ''

        except ValueError:
            print(f'[RMC] Error parsing {sentence}')

        # return sog, cmg, date_of_fix, data_validity, pos_mode_indicator
        return self.sog, self.cmg, self.date, self.time, sentence[2], self.PosMode

    @staticmethod
    def create(sentence):
        # Default, invalid fix
        fix_quality = '0'
        gps_time = ''
        dd_longitude_degrees = 0
        dd_latitude_degrees = 0
        altitude3 = 0