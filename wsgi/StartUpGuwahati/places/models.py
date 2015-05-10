"""Models for the places APIs."""

from django.db import models
from django.conf import settings

from users.models import User

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
    latitude = models.DecimalField(null=True, max_digits=9, decimal_places=7)
    longitude = models.DecimalField(null=True, max_digits=9, decimal_places=7)
    parent_locality = models.ForeignKey(
            'self',
            null=True,
            on_delete=models.SET_NULL)

    def get_latlong(self):
        """Gets the lat long for the place.
        If lat long is not available, then queries its localityid.
        If the locality id is not available, queries google geodata."""

        latitude = self.latitude
        longitude = self.longitude

        if latitude and longitude:
            return (latitude, longitude)

        # hit the web
        latLongs = cf.get_coords_from_address(
                self.locality_name,
                city=self.city.city_name)

        if latLongs:
            # save if found
            self.latitude, self.longitude = latLongs
            try:
                self.save()
            except:
                pass
            return latLongs

        return False

    def __str__(self):
        return "{0}. {1}".format(self.pk, self.locality_name)


class PlaceFacilities(models.Model):
    """Facilities for a place."""

    facility_name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)


# class PlaceFacilitiesMap(models.Model):
#     """Mapping between a place and a facility."""


class Place(models.Model):
    """Model to hold information about a place."""

    place_name = models.CharField(max_length=50)
    latitude = models.DecimalField(null=True, max_digits=9, decimal_places=7)
    longitude = models.DecimalField(null=True, max_digits=9, decimal_places=7)
    street = models.CharField(null=True, max_length=100)
    locality = models.ForeignKey(Locality, on_delete=models.PROTECT)
    is_covered = models.NullBooleanField(null=True)
    is_private = models.BooleanField(default=True)
    createdon = models.DateTimeField(auto_now_add=True, null=True)
    modifiedon = models.DateTimeField(auto_now=True, null=True)

    facilities = models.ManyToManyField(PlaceFacilities)

    def get_places_nearby(self, radius=2):
        """Gets all places which are at a distance of n kms."""

        res = self.get_latlong()
        if not res:
            return False

        latitude, longitude = res

        # get bounding box first
        latInc, latDec, longInc, longDec = cf.get_bounding_box(
                (latitude, longitude), radius)
        # return all models inside the bounding box (who have lat long).
        return (Place
                .objects
                .exclude(pk=self.pk, latitude=None, longitude=None)
                .filter(
                    latitude__gte=latDec,
                    latitude__lte=latInc,
                    longitude__gte=longDec,
                    longitude__lte=longInc,
                    ))

    def get_latlong(self):
        """Gets the lat long for the place.
        If lat long is not available, then queries its localityid.
        If the locality id is not available, queries google geodata."""

        latitude = self.latitude
        longitude = self.longitude

        if latitude and longitude:
            return (latitude, longitude)

        return self.locality.get_latlong()

    def save(self, *args, **kwargs):
        """If lat long is not passed, then try to get it from the locality.
        Likewise, if locality is not passed, get it from the latitude
        and logitude."""

        latLongs = self.get_latlong()
        if latLongs:
            self.latitude, self.longitude = latLongs

        super().save(*args, **kwargs)

    def __str__(self):
        return "{0}@{1} ({2}, {3})".format(
                self.place_name,
                self.locality.locality_name,
                self.latitude,
                self.longitude)


class PlaceAttributes(models.Model):
    """Abstract model to define the common functions for the models."""

    class Meta:
        abstract = True


class PrivatePlaceAttributes(PlaceAttributes):
    """Model to hold information about a private place."""

    place = models.OneToOneField(Place, primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self):
        if not self.place.is_private:
            raise Exception("Cannot map a public place "
                    "to have private attributes. (Place: {0})"
                    .format(self.place.pk))


class PublicPlaceAttributes(PlaceAttributes):
    """Model to hold information about a public place."""

    PLACE_TYPES = (
        (1, 'Hangout Spot'),
        (2, 'Free'),
        )

    place = models.OneToOneField(Place, primary_key=True)
    place_type = models.IntegerField(choices=PLACE_TYPES)

    def save(self):
        if not self.place.is_private:
            raise Exception("Cannot map a private place "
                    "to have public attributes. (Place: {0})"
                    .format(self.place.pk))


class PlaceImages(models.Model):
    """Mapping between a place and its images."""

    place = models.ForeignKey(Place)
    image = models.ImageField(upload_to='places')


def get_places_nearby(source, radius):
    """Gets the nearby places for a given lat long."""

    latitude, longitude = source

    # get bounding box first
    latInc, latDec, longInc, longDec = cf.get_bounding_box(
            (latitude, longitude), radius)
    # return all models inside the bounding box (who have lat long).
    return (models.Place
            .objects
            .exclude(latitude=None, longitude=None)
            .filter(
                latitude__gte=latDec,
                latitude__lte=latInc,
                longitude__gte=longDec,
                longitude__lte=longInc,
                ))
