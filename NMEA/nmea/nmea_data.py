'''
Various tables of data from UBlox documentation
'''

TALKER_ID = {
    'GN': 'GNSS Device',
    'GL': 'GLONASS',
    'GQ': 'QZSS',
    'GP': 'GPS Device',
    'GB': 'Beidou',
    'GA': 'Galileo'

}

SENTENCE_ID = {
    'RMC': 'Recommended minimum data',
    'GGA': 'Global positioning system fix data',
    'GST': 'GNSS pseudorange error statistics',
    'GSV': 'GNSS satellites in view',
    'THS': 'True heading and status',
    'TXT': 'Text',
    'VTG': 'Course over ground and ground speed'

}

GGA_Quality = {
    '0': 'No position',
    '1': '2D GNSS',
    '2': '3D GNSS/DGPS',
    '3': 'PPS Fix',
    '4': 'RTK Fixed',
    '5': 'RTK Float',
    '6': 'Dead Reckoning'
}

RMC_PosMode = {
    'N': 'No fix',
    'E': 'Estimated/dead reckoning fix',
    'A': 'Autonomous GNSS fix',
    'D': 'Differential GNSS fix',
    'F': 'RTK float',
    'R': 'RTK fixed'
}

THS_ModeIndicator = {
    'A': 'Autonomous',
    'E': 'Estimated (dead reckoning)',
    'M': 'Manual input',
    'S': 'Simulator',
    'V': 'Data not valid'
}