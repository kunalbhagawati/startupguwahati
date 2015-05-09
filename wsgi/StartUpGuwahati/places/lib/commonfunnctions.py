"""Holds the common functions for the places API."""

import math


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
