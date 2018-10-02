# Geospatial Tools for IPUMS Census Data

## Setup

This repository was developed using Python version `3.6.5`.
You can install the required dependencies via `pip install -r requirements.txt`.


## Getting a Census Extract

[1] Create an account on the [IPUMS USA site](https://usa.ipums.org/usa/index.shtml)

[2] Go to the main page and click “select data”

[3] Click the blue box labeled “select samples”

[4] Change the samples from the default to the 5% of the 1930 census

* Unchecking “Default sample from each year”
* Checking “1930 5%”
* Clicking “Submit sample selections”

[5] Select the attributes you want in the dataset

 * Location data: "Household" -> "Historical Technical" -> "Enumeration District"
 * Need to also add `STATEICP`, `COUNTY`
 * (Optional) Categorical and numerical data under Person

[6] View cart

[7] Change the data format to be .csv

[8] Create data extract



## Getting County Boundary Information

[1] Create an account on the [IPUMS NHGIS site](https://www.nhgis.org/)

[2] Click "Get Data" on the homepage

[3] Click "Years", "1930", and submit

[4] Click the plus corresponding to the row "Geographic Level: County" and "Basis: 2008 TIGER/Line+"

[5] Click continue in the top right of the page and submit


## Project Structure

The following should be your directory structure.

* `main.py`
* `/data`
  * `/1930`
    * `usa_1930_5.csv` // Required from census extract
    * `/gis`
      * `US_county_1930_conflated.shp` // Required from GIS extract
      * `US_county_1930_conflated.prj` // Required from GIS extract

      * `US_county_1930_conflated.dbf`
      * `US_county_1930_conflated.sbn`
      * `US_county_1930_conflated.sbx`
      * `US_county_1930_conflated.shp.xml`
      * `US_county_1930_conflated.shx`

Finally, simply run `main.py`.
