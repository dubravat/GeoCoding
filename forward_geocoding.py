# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
***************************************************************************
forward_geocoding.py
---------------------
Date                 : May 2022
Copyright            : (C) 2022 by Taras Dubrava
Email                : tarasdubrava at yahoo dot com
***************************************************************************
*                                                                         *
*   Applying forward geocoding in a CSV file represented as a DataFrame.  *
*   It uses five geocoders, namely: ArcGIS, Bing, GoogleV3, Here, and     *
*   Nominatim taken from the GeoPy library.                               *
*   For some geocoders an API key must be specified.                      *
*   Geocoding of each record is done with one second delay.               *
*   Each geocoded DataFrame will be exported as a CSV file with a         *
*   corresponding name, based on the title of the geocoding service.      *
*                                                                         *
***************************************************************************
"""

__author__ = 'Taras Dubrava'
__date__ = 'May 2022'
__copyright__ = '(C) 2022, Taras Dubrava'

# imports
import yaml
import pandas as pd
from geopy.geocoders import (ArcGIS, Bing, GoogleV3, Here, Nominatim)
from geopy.extra.rate_limiter import RateLimiter

# accessing a file with authentication credentials
with open("authentication.yaml", "r") as file:
    auth_file = yaml.safe_load(file)


def forward_geocoding(geocoder: str = None, address: str = None) -> tuple or None:
    """
    Geocode an address with a specified geocoding service.
    forward_geocoding(None, 'Warsaw') -> (52.231958, 21.006725)
    GeoPy Documentation: https://geopy.readthedocs.io/en/stable/
    Parameters:
    ==========
    :param geocoder: provider of a geocoder, Nominatim is the default.
    :param address: an address e.g. 'Ulica Franje Račkog 12, 10000, Zagreb, Croatia'.
    Returns:
    ==========
    :return: a tuple with latitude and longitude as floats with 6 digits after comma each.
    """
    if address:
        if geocoder == 'arcgis':
            geolocator = ArcGIS(username=auth_file['arcgis']['username'],
                                password=auth_file['arcgis']['password'],
                                referer='geocoding')
        elif geocoder == 'bing':
            geolocator = Bing(api_key=auth_file['bing api key'])
        elif geocoder == 'google':
            geolocator = GoogleV3(api_key=auth_file['google geocoding api key'])
        elif geocoder == 'here':
            geolocator = Here(apikey=auth_file['here api key'])
        else:
            geolocator = Nominatim(user_agent='geocoding')

        forward = RateLimiter(geolocator.geocode, min_delay_seconds=1)

        try:
            location = forward(address)
            return (float(format(location.latitude, '.6f')), float(format(location.longitude, '.6f')))
        except (AttributeError, KeyError, ValueError):
            return None

absolute_path_to_csv_file = 'D:/GeoCoding/input_csv_file/geocoding.csv'
# reading a CSV file with addresses
df_from_input_csv = pd.read_csv(absolute_path_to_csv_file, delimiter=';', encoding='utf8')

# specifying a path for output files
path_for_export = 'geocoded_csv_files/'

# applying forward geocoding with a different service to the same CSV file
for service in ['arcgis', 'bing', 'google', 'here', 'nominatim']:
    df_from_input_csv['location'] = df_from_input_csv.apply(lambda row: forward_geocoding(geocoder=service, address=row['address']), axis=1)
    df_from_input_csv['lat'] = df_from_input_csv['location'].str[0]
    df_from_input_csv['lon'] = df_from_input_csv['location'].str[1]
    df_from_input_csv.drop(['location'], axis=1)
    #df_from_input_csv.to_csv(path_for_export + f'{service}.csv', encoding='utf-8', index=False)

if __name__ == '__main__':
    print('Done!')
