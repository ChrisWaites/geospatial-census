import csv
import os

from states import states
from counties import counties
from coords import coords

file_name = 'data/1930/usa_1930_5.csv'
out_file_name = 'out/out.csv'

os.makedirs('out', exist_ok=True)

with open(out_file_name, 'w') as g:
    with open(file_name) as f:
        reader = csv.DictReader(f)
        writer = csv.DictWriter(g, reader.fieldnames + ['latitude', 'longitude'])

        print('Beginning Conversion...')

        for line in reader:
            try:
                state_id = line['STATEICP']
                county_id = line['COUNTY']
                enum_dist_id = line['ENUMDIST']

                state = states[line['STATEICP']]
                county = counties[line['STATEICP']][line['COUNTY']]
                enum_dist = line['ENUMDIST']
                latitude, longitude = coords[state_id][county_id]

                line['latitude'] = latitude
                line['longitude'] = longitude

                writer.writerow(line)
            except:
                pass

