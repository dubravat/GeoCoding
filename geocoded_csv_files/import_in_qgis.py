# !/usr/bin/env python
"""
***************************************************************************
import_in_qgis.py
---------------------
Date                 : May 2022
Copyright            : (C) 2022 by Taras Dubrava
Email                : tarasdubrava at yahoo dot com
***************************************************************************
*                                                                         *
*   For importing several CSV files into QGIS at once.                    *
*   The root folder should be determined as well as other custom          *
*   specifications in the settings section.                               *
*                                                                         *
***************************************************************************
"""
__author__ = 'Taras Dubrava'
__date__ = 'May 2022'
__copyright__ = '(C) 2022, Taras Dubrava'

# imports
import os
from qgis.core import (QgsVectorLayer, QgsProject)

# settings
absolute_path_to_csv_files = 'D:/GeoCoding/geocoded_csv_files/'
encoding = 'UTF-8'
delimiter = ','
decimal = '.'
crs = 'epsg:4326'
x = 'lon'
y = 'lat'

# getting all csv files in the import folder
files_names = filter(lambda x: x.endswith('.csv'), os.listdir(absolute_path_to_csv_files))

# importing each CSV file in the import folder
for file in files_names:
    absolute_path_to_csv_file = absolute_path_to_csv_files + file
    uri = f"file://{absolute_path_to_csv_file}?encoding={encoding}&delimiter={delimiter}&decimalPoint={decimal}&crs={crs}&xField={x}&yField={y}"

    # making a Vector Layer
    base = os.path.basename(absolute_path_to_csv_file)
    point_layer_name = os.path.splitext(base)[0]
    layer = QgsVectorLayer(uri, point_layer_name, "delimitedtext")

    # checking if the layer is valid
    if not layer.isValid():
        print("Layer not loaded")

    # adding the layer
    QgsProject.instance().addMapLayer(layer)
