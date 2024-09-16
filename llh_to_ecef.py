# script_name.py
#
# Usage: python3 script_name.py arg1 arg2 ...
#  Text explaining script usage
# Parameters:
#  arg1: description of argument 1
#  arg2: description of argument 2
#  ...
# Output:
#  A description of the script output
#
# Written by Jayden Warren
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import sys # argv
import math

# "constants"
e_E = 0.081819221456
r_E_km = 6378.1363

# helper functions
def calc_denom(ecc,lat_rad):
    return math.sqrt(1.0-(ecc**2)*(math.sin(lat_rad)**2))

## function description
    # def calc_denom(ecc,lat_rad):
        #Shortcut for the denominateor found in CE and SE

# initialize script arguments
lat_deg = float('nan') # Longitude in Degrees
lon_deg = float('nan') # Latitude in Degrees
hae_km = float('nan') # Height above ellipsoid in km

# parse script arguments
if len(sys.argv)==4:
    lat_deg = float(sys.argv[1])
    lon_deg = float(sys.argv[2])
    hae_km  = float(sys.argv[3])
else:
    print(\
     'Usage: '\
     'python3 llh_to_ecef.py lon_deg lat_deg hae_km'\
    )
    exit()

lat_rad = math.radians(lat_deg)
lon_rad = math.radians(lon_deg)

# write script below this line
denom = calc_denom(e_E,lat_rad)
C_E = r_E_km/denom
#S_E = (r_E_km*(1-e_E*e_E))/denom
r_x_km = (C_E+hae_km)*math.cos(lat_rad)*math.cos(lon_rad)
r_y_km = (C_E+hae_km)*math.cos(lat_rad)*math.sin(lon_rad)
r_z_km = (C_E*(1-e_E**2)+hae_km)*math.sin(lat_rad)
#r = math.sqrt(r_x_km*r_x_km+r_y_km*r_y_km+r_z_km*r_z_km)


print(f"r_x_km {r_x_km}")
print(f"r_y_km {r_y_km}")
print(f"r_z_km {r_z_km}")