from datetime import datetime
import sys, csv


def path_name():
    # Operating system dependent stuff
    this_os = sys.platform
    if this_os == 'win32':
        return './logfiles/'
    elif this_os == 'linux':
        return '/home/pi/logfiles/'
    else:
        print(f'Unsupported OS: {this_os}')
        exit(0)


def log_file_name(extension):
    """
    Create a file name in the logfiles directory, based on current data and time
    Requires the computer to have an RTC or synched clock
    """
    now = datetime.now()
    # Linux
    file_name = '%0.4d%0.2d%0.2d-%0.2d%0.2d%0.2d' % (now.year, now.month, now.day, now.hour, now.minute, now.second)
    return file_name + extension


