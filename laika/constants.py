# These are all from IS-GPS-200G unless otherwise noted

SPEED_OF_LIGHT = 2.99792458e8  # m/s

# Physical parameters of the Earth
EARTH_GM = 3.986005e14  # m^3/s^2 (gravitational constant * mass of earth)
EARTH_RADIUS = 6.3781e6  # m
EARTH_ROTATION_RATE = 7.2921151467e-005  # rad/s (WGS84 earth rotation rate)

# GPS system parameters:
GPS_L1 = l1 = 1.57542e9  # Hz
GPS_L2 = l2 = 1.22760e9  # Hz

#GLONASS system parameters
#TODO this is old convention
GLONASS_L1 = 1.602e9
GLONASS_L1_DELTA = 0.5625e6
GLONASS_L2 = 1.246e9
GLONASS_L2_DELTA = 0.4375e6

SECS_IN_MIN = 60
SECS_IN_HR = 60*SECS_IN_MIN
SECS_IN_DAY = 24*SECS_IN_HR
SECS_IN_WEEK = 7*SECS_IN_DAY
SECS_IN_YEAR = 365*SECS_IN_DAY
