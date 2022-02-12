from nmea.nmea_data import THS_ModeIndicator

# THS - True heading and status
# GNTHS,350.74,A*1C
# True heading in degrees
# Mode Indicator
# Checksum


class ths():
    # Constructor
    def __init__(self):
        # Switch this on for verbose processing
        self.debug = 1
        self.mode_indicator = ''
        self.heading_true = 0

    def parse(self, sentence):
        if self.debug == 1:
            print(f'Debug THS:{sentence}')

        list_of_values = sentence.split(',')
        try:
            # Check if valid sentence
            if list_of_values[2] != 'V':
                self.mode_indicator = list_of_values[2]
                self.heading_true = float(list_of_values[1])

        except ValueError:
            print(f'[THS] Error parsing {sentence}')
        except:
            print(f'Debug THS:{sentence}')

        return self.mode_indicator, self.heading_true,

    @staticmethod
    def create(sentence):
        # Default, invalid fix
        fix_quality = '0'
        gps_time = ''
        dd_longitude_degrees = 0
        dd_latitude_degrees = 0
        altitude3 = 0