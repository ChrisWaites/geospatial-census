import csv
import os

from states import states
from counties import counties
from coords import coords

file_name = 'data/usa_00001.csv'
out_file_name = 'out/coordinates.csv'

os.makedirs('out', exist_ok=True)

with open(out_file_name, 'w') as g:
    with open(file_name) as f:
        reader = csv.DictReader(f)
        for line in reader:
            try:
                state_id = line['STATEICP']
                county_id = line['COUNTY']
                enum_dist_id = line['ENUMDIST']

                state = states[line['STATEICP']]
                county = counties[line['STATEICP']][line['COUNTY']]
                enum_dist = line['ENUMDIST']
                latitude, longitude = coords[state_id][county_id]

                g.write('{}, {}\n'.format(latitude, longitude))
            except:
                pass

