"""Holds the common functions for the places API."""

import math
import requests
from django.conf import settings


def distance(origin, destination):
    """Takes the source (lat, long) and destination (lat, long)
    and gives the distance between them."""

    lat1, lon1 = origin
    lat2, lon2 = destination
    RADIUS = 6371    # earths radius. Unchangable

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = RADIUS * c

    return d


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
