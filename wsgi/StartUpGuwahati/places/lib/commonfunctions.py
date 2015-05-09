"""Holds the common functions for the places API."""

import math
import requests
import geopy
from geopy.distance import VincentyDistance
from geopy.distance import vincenty

from django.conf import settings


def distance(origin, destination):
    """Takes the source (lat, long) and destination (lat, long)
    and gives the distance between them."""

    return vincenty(origin, destination)


def offset_latlong(origin, distance, bearing):
    """Offsets the lat long by an n distance.
    bearing in degrees, distance in kilometers"""

    origin = geopy.Point(origin[0], origin[1])
    destination = VincentyDistance(kilometers=distance).destination(
            origin, bearing)

    return (destination.latitude, destination.longitude)


def get_bounding_box(origin, distance):
    """Gets the bounding box i.e. the lat+dist, lat-dist, long+dist, long-dist.
    """

    latInc = offset_latlong(origin, distance, 0)[0]
    latDec = offset_latlong(origin, distance, 180)[0]
    longInc = offset_latlong(origin, distance, 90)[1]
    longDec = offset_latlong(origin, distance, 270)[1]

    return (latInc, longInc, latDec, longDec)


def get_coords_from_address(address):
    """Gets the lat and long from a given place. Hits google directly."""

    url = "https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}".format(address, settings.GOOGLE_API_KEY)
    res = requests.get(url)
    if res.status_code//100 == 5:
        # Google internat server error
        raise Exception(500)
    if res.status_code//100 == 4:
        # Bad Request, Auth Failed
        raise Exception(400)

    resDict = res.json()
    if not resDict['results']:
        return False
    latlongs = set()
    for pDict in resDict['results']:   # may contain multiple
        location = pDict['geometry']['location']
        latitude = location['lat']
        longitude = location['lng']
        latlongs.add((latitude, longitude))

    return latlongs
