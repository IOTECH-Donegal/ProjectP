# GNSS pseudorange error statistics
    # GNGST, 120112.00, 34, 0.011, 0.0065, 38, 0.010, 0.010, 0.010 * 76
    # 1 - Fix taken at in UTC as hhmmss.ss
    # 2 - RMS value of the standard deviation of the ranges
    # 3 - Standard deviation of semi-major axis
    # 4 - Standard deviation of semi-minor axis
    # 5 - Orientation of semi-major axis
    # 6 - Standard deviation of latitude error
    # 7 - Standard deviation of longitude error
    # 8 - Standard deviation of altitude error

class gst():
    # Constructor
    def __init__(self):
        # Switch this on for verbose processing
        self.debug = 1
        self.sigma_latitude = '0'
        self.sigma_longitude = '0'
        self.sigma_altitude = '0'

    def parse(self, sentence):
        try:
            list_of_values = sentence.split(',')
            self.sigma_latitude = float(list_of_values[6])
            self.sigma_longitude = float(list_of_values[7])
            sigma_altitude_and_crc = list_of_values[8].split('*')
            self.sigma_altitude = float(sigma_altitude_and_crc[0])

        except ValueError:
            print(f'[GST] Error parsing {sentence}')

        return self.sigma_latitude, self.sigma_longitude, self.sigma_altitude

    @staticmethod
    def create(sentence):
        # Default, invalid fix
        fix_quality = '0'
        gps_time = ''
        dd_longitude_degrees = 0
        dd_latitude_degrees = 0
        altitude3 = 0