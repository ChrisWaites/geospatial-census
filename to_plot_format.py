from csv import DictReader, DictWriter
from collections import defaultdict

reader = DictReader(open('data/1940/usa_1940_100.csv'))
counts = defaultdict(lambda: defaultdict(int))

for line in reader:
    state = line['STATEFIP']
    county = line['COUNTY'][:-1]
    counts[state][county] += 1

writer = DictWriter(open('updated.csv', 'w'), ['State FIPS Code', 'County FIPS Code', 'Population'])
writer.writerow({'State FIPS Code': 'State FIPS Code', 'County FIPS Code': 'County FIPS Code', 'Population': 'Population'})

for state in sorted(counts):
    for county in sorted(counts[state]):
        writer.writerow({'State FIPS Code': state, 'County FIPS Code': county, 'Population': counts[state][county]})

print('done.')
