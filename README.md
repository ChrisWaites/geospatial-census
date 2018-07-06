# Geospatial Tools for IPUMS Census Data

First, create an account with [IPUMS USA](https://usa.ipums.org/usa/index.shtml).

Next, create an extract. The sample chosen was `1930s 5%`.

Your extract should include the following attributes, and be in `.csv` format.

* `STATEICP`
* `COUNTY`

Next, go to the [IPUMS NHGIS](https://www.nhgis.org/) to extract GIS information.

Create a data extract for county GIS information for the year `1930`.

The following should be your directory structure.

* `main.py`
* `/data`
  * `_.csv`
  * `/gis`
    * `_.shp`
    * `_.prj`

Finally, simply run `main.py`.
