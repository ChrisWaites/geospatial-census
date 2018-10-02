# Geospatial Tools for IPUMS Census Data

## Getting a Census Extract

[1] Create an account on the [IPUMS USA site](https://usa.ipums.org/usa/index.shtml)

[2] Go to the main page and click “select data”

[3] Click the blue box labeled “select samples”

[4] Change the samples from the default to the 5% of the 1930 census

* Unchecking “default sample from each year”
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

[2] Click "get data" on the homepage

[3] Click "years", "1930", and submit

[4] Click the plus next to the row "Year: 1930", "Geographic Level: County" and "Basis: 2008 TIGER/Line+"

[5] Click continue in the top right of the page and submit


## Project Structure

The following should be your directory structure.

* `main.py`
* `/data`
  * `_.csv`
  * `/gis`
    * `_.shp`
    * `_.prj`

Finally, simply run `main.py`.
