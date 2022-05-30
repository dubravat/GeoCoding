# Geocoding for all: <br> A subtle introduction to Geocoding
## (C) Taras Dubrava
### May 2022

----
Presentation : [Geocoding for all](geocoding_for_all.pdf) <br>
QGIS wiki Page :  https://github.com/qgis/QGIS/wiki/QOD-April-2022 <br>
Video on YouTube : https://youtu.be/G-rQKuSSCkg
----

This repository contains the following files:
1. Python files:
   - `forward_geocoding.py`: for forward geocoding in CSV file
   - `reverse_geocoding.py`: for reverse geocoding (just a function)
   - `geocoded_csv_files/import_in_qgis.py`: for importing several CSV files at once into QGIS
2. A folder with an input CSV file `geocoding.csv` with several modifications of it: `input_csv_file/`
3. A folder with geocoded CSV files: `geocoded_csv_files/`

### P.S. Remember that the repo does not include the YAML file with credentials (authentication.yaml) required for geocoding service authentication.
