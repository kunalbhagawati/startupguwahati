from django.db import models
import math


def distance(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371    # earrths radius

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d


class Country(models.Model):
    country_name = models.CharField(max_length=50)

    def __str__(self):
        return self.country_name


class State(models.Model):
    state_name = models.CharField(max_length=255)
    country = models.ForeignKey(
            Country,
            on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.state_name


class City(models.Model):
    city_name = models.CharField(max_length=255)
    state = models.ForeignKey(
            State,
            on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.city_name


class Locality(models.Model):
    locality_name = models.CharField(max_length=255)
    city = models.ForeignKey(
            City,
            on_delete=models.PROTECT)
    latitude = models.DecimalField(null=True, max_digits=9, decimal_places=2)
    longitude = models.DecimalField(null=True, max_digits=9, decimal_places=2)
    parent_locality = models.ForeignKey(
            'self',
            null=True,
            on_delete=models.SET_NULL)

    def __str__(self):
        return self.locality_name


class Place(models.Model):
    """Abstract model to hold information about a place."""

    place_name = models.CharField(max_length=50)
    latitude = models.DecimalField(null=True, max_digits=9, decimal_places=2)
    longitude = models.DecimalField(null=True, max_digits=9, decimal_places=2)
    street = models.CharField(null=True, max_length=100)
    locality = models.ForeignKey(Locality, on_delete=models.PROTECT)

    is_place_covered = models.NullBooleanField(null=True)

    def __str__(self):
        return "{0}@({1}, {2})".format(
                self.place_name, self.latitude, self.longitude)

    class Meta:
        abstract = True


class PrivatePlace(Place):
    """Model to hold information about a private place."""


class PublicPlace(Place):
    """Model to hold information about a public place."""

    PLACE_TYPES = (
        (1, 'Hangout Spot'),
        (2, 'Free'),
        )

    place_type = models.IntegerField(choices=PLACE_TYPES)


# class PlaceFilters(models.Model):
#     """Filters for a place."""

#     place = models.ForeignKey(Place, on_delete=models.CASCADE)

#     class Meta:
#         abstract = True


# class PlaceQualities(models.Model):
#     """Master for the qualities a place can have."""

#     quality_name = models.ForeignKey()
