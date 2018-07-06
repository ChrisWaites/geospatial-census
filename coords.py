import fiona
import pyproj 
from osgeo import osr
from collections import defaultdict

file_name = 'data/gis/US_county_1930_conflated.shp'

in_proj = pyproj.Proj("+proj=aea +lat_1=29.5 +lat_2=45.5 +lat_0=37.5 +lon_0=-96 +x_0=0 +y_0=0 +datum=NAD83 +units=m +no_defs")
out_proj = pyproj.Proj("+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs")

shape = fiona.open(file_name)

coords = defaultdict(dict)

for line in shape:
    properties = line['properties']

    state_id = properties['ICPSRST']
    county_id = properties['ICPSRCTY']
    x_coord = properties['X_CENTROID']
    y_coord = properties['Y_CENTROID']

    coords[state_id][county_id] = pyproj.transform(in_proj, out_proj, x_coord, y_coord)[::-1]

