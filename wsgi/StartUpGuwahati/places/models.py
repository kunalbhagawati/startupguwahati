"""Models for the places APIs."""

from django.db import models

from .lib import commonfunctions as cf


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


class PlaceFacilities(models.Model):
    """Facilities for a place."""

    facility_name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE)


# class PlaceFacilitiesMap(models.Model):
#     """Mapping between a place and a facility."""


class Place(models.Model):
    """Abstract model to hold information about a place."""

    place_name = models.CharField(max_length=50)
    latitude = models.DecimalField(null=True, max_digits=9, decimal_places=2)
    longitude = models.DecimalField(null=True, max_digits=9, decimal_places=2)
    street = models.CharField(null=True, max_length=100)
    locality = models.ForeignKey(Locality, on_delete=models.PROTECT)
    is_place_covered = models.NullBooleanField(null=True)

    facilities = models.ManyToManyField(PlaceFacilities)

    def get_places_nearby(self, radius=2):
        """Gets all places which are at a distance of n kms."""

        pass

    def save(self):
        """If lat long is not passed, then try to get it from the locality.
        Likewise, if locality is not passed, get it from the latitude
        and logitude."""

        pass

    def __str__(self):
        return "{0}@({1}, {2})".format(
                self.place_name, self.latitude, self.longitude)

    class Meta:
        abstract = True


class PrivatePlace(Place):
    """Model to hold information about a private place."""

    owner = models.IntegerField()   # set to foreign key later


class PublicPlace(Place):
    """Model to hold information about a public place."""

    PLACE_TYPES = (
        (1, 'Hangout Spot'),
        (2, 'Free'),
        )

    place_type = models.IntegerField(choices=PLACE_TYPES)
