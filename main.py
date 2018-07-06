import itertools
import csv
from collections import defaultdict
import time

from states import states
from cities import cities
from counties import counties
from coords import coords

file_name = 'data/usa_00006.csv'

with open('coordinates.csv', 'w') as g:
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
                x, y = coords[state_id][county_id]

                g.write('{}, {}\n'.format(x, y))
            except:
                pass

