from collections import defaultdict
import csv

file_name = 'data/counties.csv'

counties = defaultdict(dict)

with open(file_name) as f:
    for line in csv.DictReader(f):
        counties[line['STATEICP']][line['COUNTY']] = line['County']

