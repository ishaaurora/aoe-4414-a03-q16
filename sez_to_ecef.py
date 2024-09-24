# sez_to_ecef.py
#
# Usage: python3 sez_to_ecef.py o_lat_deg o_lon_deg o_hae_km s_km e_km z_km
#  Using the above parameters to covert from sez to ecef

# Parameters:
#  o_lat_deg: observatory/origin latitude in degrees
#  o_lon_deg: observatory/origin longitude in degrees
#  o_hae_km: observatory/origin height above the ellipsoid in km 
#  s_km: SEZ south-component in km
#  e_km: SEZ east-component in km
#  z_km: SEZ z-component in km
#  ...
# Output:
#  prints ecef x,y, and z components in km
#
# Written by Isha Aurora
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv
import math
import numpy as np

# "constants"
R_E_KM = 6378.1363
E_E = 0.081819221456

# helper functions
def calc_denom(ecc,lat_rad):
   
   return math.sqrt(1 - (ecc*ecc)*(math.sin(lat_rad))**2)

## function description
# def calc_something(param1, param2):
#   pass


# initialize script arguments
o_lat_deg= float('nan')
o_lon_deg= float('nan')
o_hae_km=float('nan')
s_km= float('nan')
e_km= float('nan')
z_km= float('nan')


# parse script arguments
if len(sys.argv)==7:
   o_lat_deg = float(sys.argv[1])
   o_lon_deg = float(sys.argv[2])
   o_hae_km = float(sys.argv[3])
   s_km = float(sys.argv[4])
   e_km = float(sys.argv[5])
   z_km = float(sys.argv[6])

else:
   print(\
    'Usage: '\
    'python3 sez_to_ecef.py o_lat_deg o_lon_deg o_hae_km s_km e_km z_km'\
   )
   exit()

#in rads
lon_rad = o_lon_deg*math.pi/180
lat_rad = o_lat_deg*math.pi/180

# write script below this line

R_y = np.array([[math.sin(lat_rad), 0, math.cos(lat_rad)], [0,1,0],[-math.cos(lat_rad), 0, math.sin(lat_rad)]])
sez_vec = np.array([[s_km],[e_km],[z_km]])
first_rot = R_y.dot(sez_vec)
R_z = np.array([[math.cos(lon_rad),-math.sin(lon_rad),0], [math.sin(lon_rad), math.cos(lon_rad),0], [0,0,1]])
sec_rot = R_z.dot(first_rot)

ecef_x_km = sec_rot[0]
ecef_y_km = sec_rot[1]
ecef_z_km = sec_rot[2]

#print results
print(ecef_x_km)
print(ecef_y_km)
print(ecef_z_km)

#using denom for Ce and Se
#denom = calc_denom(E_E, lat_rad)
#Ce = R_E_KM/denom 
#Se = (R_E_KM*(1-E_E**2))/denom

#first rotation 
#rx_km = (Ce+o_hae_km)*math.cos(lat_rad)*math.cos(lon_rad)
#ry_km = (Ce+o_hae_km)*math.cos(lat_rad)*math.sin(lon_rad)
#rz_km = (Se+o_hae_km)*math.sin(lat_rad)

#r_x_ecef = math.cos(lon_rad)*math.sin(lat_rad)*s_km + math.cos(lon_rad)*math.cos(lat_rad)*z_km - math.sin(lon_rad)*e_km
#r_y_ecef = math.sin(lon_rad)*math.sin(lat_rad)*s_km + math.sin(lon_rad)*math.cos(lat_rad)*z_km + math.cos(lon_rad)*e_km
#r_z_ecef = -math.cos(lat_rad)*s_km + math.sin(lat_rad)*z_km