# Geospatial Tools for IPUMS Census Data

## Getting a Census Extract

[1] Create an account on the [IPUMS USA site](https://usa.ipums.org/usa/index.shtml)

[2] Go to the main page and click “select data”

[3] Click the blue box labeled “select samples”

[4]Change the samples from default to the full 1940 census by…

* Unchecking “default sample from each year”
* Clicking on the USA full count tab
* Checking “1930 5%”
* Clicking “Submit sample selections”

[5] Select the attributes you want in the dataset

 * Geospatial data: Household -> Historical Technical -> Enumeration District
 * Need to also add `STATEICP`, `COUNTY`
 * Plenty of categorical/numerical under Person -> …

[6] View cart

[7] Create data extract

[8] Change the data format to be .csv


## Getting County Boundary Information

[1] Create an account on the [IPUMS NHGIS site](https://www.nhgis.org/).

[2] Create a data extract for county GIS information for the year `1930`.


## Project Structure

The following should be your directory structure.

* `main.py`
* `/data`
  * `_.csv`
  * `/gis`
    * `_.shp`
    * `_.prj`

Finally, simply run `main.py`.
