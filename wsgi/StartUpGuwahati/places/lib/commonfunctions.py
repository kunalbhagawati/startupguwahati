"""Holds the common functions for the places API."""

import math
import requests
import geopy
from geopy import exc as geopyExc
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

    return (latInc, latDec, longInc, longDec)


def get_coords_from_address(address, city=None):
    """Gets the lat and long from a given place. Hits google directly."""

    # attempt open maps first
    try:
        d = geopy.Nominatim(timeout=10)
        qArgs = {
            'street': address
        }
        if city:
            qArgs['city'] = city
        res = d.geocode(query=qArgs)
        if res:
            return (res.latitude, res.longitude)
    except geopyExc.GeocoderTimedOut:
        pass

    try:
        d = geopy.GoogleV3(api_key=settings.GOOGLE_API_KEY, timeout=10)
        qArgs = {
            'query': address
        }
        if city:
            qArgs['components'] = {'city': city}
        res = d.geocode(query=qArgs)
        if res:
            return (res.latitude, res.longitude)
    except geopyExc.GeocoderTimedOut:
        pass

    return False
