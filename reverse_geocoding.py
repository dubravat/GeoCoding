# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
***************************************************************************
reverse_geocoding.py
---------------------
Date                 : May 2022
Copyright            : (C) 2022 by Taras Dubrava
Email                : tarasdubrava at yahoo dot com
***************************************************************************
*                                                                         *
*   Applying reverse geocoding. It uses five geocoders, namely: ArcGIS,   *
*   Bing, GoogleV3, Here, and Nominatim taken from the GeoPy library.     *
*   For some geocoders an API key must be specified.                      *
*   Reverse geocoding of each pair is done with one-second delay.         *
*   Additionally coordinates are wrapped into a geodetic Point.           *
*                                                                         *
***************************************************************************
"""

__author__ = 'Taras Dubrava'
__date__ = 'May 2022'
__copyright__ = '(C) 2022, Taras Dubrava'

# imports
import yaml
from geopy.geocoders import (ArcGIS, Bing, GoogleV3, Here, Nominatim)
from geopy.extra.rate_limiter import RateLimiter
from geopy.point import Point

# accessing a file with authentication credentials
with open("authentication.yaml", "r") as file:
    auth_file = yaml.safe_load(file)


def reverse_geocoding(geocoder: str = None, lat: float = None, lon: float = None) -> str or None:
    """
    Reverse geocode coordinates with a specified geocoding service.
    reverse_geocoding('here',30.197535,-97.662015) -> '3212 Emma Browning Ave, Austin, TX 78719, United States, Austin, TX 78719, USA'
    GeoPy Documentation: https://geopy.readthedocs.io/en/stable/
    Parameters:
    ==========
    :param geocoder: provider of a geocoder, Nominatim is the default.
    :param lat: the latitude coordinate.
    :param lon: the longitude coordinate.
    Returns:
    ==========
    :return: a string with an address.
    """

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

    reverse = RateLimiter(geolocator.reverse, min_delay_seconds=1)
    point = Point(lat, lon)

    try:
        address = reverse(point)
        return address
    except (AttributeError, KeyError, ValueError):
        return None


if __name__ == '__main__':
    print('Done!')
