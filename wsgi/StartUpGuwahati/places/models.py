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
    latitude = models.DecimalField(null=True, max_digits=9, decimal_places=2)
    longitude = models.DecimalField(null=True, max_digits=9, decimal_places=2)
    parent_locality = models.ForeignKey(
            'self',
            null=True,
            on_delete=models.SET_NULL)

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
    latitude = models.DecimalField(null=True, max_digits=9, decimal_places=2)
    longitude = models.DecimalField(null=True, max_digits=9, decimal_places=2)
    street = models.CharField(null=True, max_length=100)
    locality = models.ForeignKey(Locality, on_delete=models.PROTECT)
    is_place_covered = models.NullBooleanField(null=True)
    is_place_private = models.BooleanField(default=True)
    createdon = models.DateTimeField(auto_now_add=True, null=True)
    modifiedon = models.DateTimeField(auto_now=True, null=True)

    facilities = models.ManyToManyField(PlaceFacilities)

    def get_places_nearby(self, radius=2):
        """Gets all places which are at a distance of n kms."""

        pass

    def get_latlong(self,):
        """Gets the lat long for the place.
        If lat long is not available, then queries its localityid.
        If the locality id is not available, queries google geodata."""

        latitude = self.latitude
        longitude = self.longitude

        if not latitude or not longitude:
            # fetch from locality
            latitude = self.locality.latitude
            longitude = self.locality.longitude

        if not latitude or not longitude:
            # hit google
            latLongs = cf.get_coords_from_address(self.locality.locality_name)
            if not latLongs:
                return False

            latLongs = tuple(latLongs)
            latitude = latLongs[0][0]
            longitude = latLongs[0][1]

        return (latitude, longitude)

    def save(self):
        """If lat long is not passed, then try to get it from the locality.
        Likewise, if locality is not passed, get it from the latitude
        and logitude."""

        if not self.latitude or self.longitude:
            latLongs = cf.get_coords_from_address(self.locality.locality_name)
            if not latLongs:
                raise Exception("Could not find lat long for "
                        "locality: {0}".format(self.locality))
            else:
                latLongs = tuple(latLongs)
                self.latitude = latLongs[0][0]
                self.longitude = latLongs[0][1]

    def __str__(self):
        return "{0}@({1}, {2})".format(
                self.place_name, self.latitude, self.longitude)


class PlaceAttributes(models.Model):
    """Abstract model to define the common functions for the models."""

    class Meta:
        abstract = True


class PrivatePlaceAttributes(PlaceAttributes):
    """Model to hold information about a private place."""

    place = models.OneToOneField(Place, primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self):
        if not self.place.is_place_private:
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
        if not self.place.is_place_private:
            raise Exception("Cannot map a private place "
                    "to have public attributes. (Place: {0})"
                    .format(self.place.pk))

# def get_image_name(inst, filename):
#     """Gets the filename in the format."""

#     dirName = 'homepagebanners'
#     ext = filename.split(".")[-1]
#     localeTypeName = inst.get_localetype_display()
#     return "{0}/{1}/{2}_{3}.{4}".format(
#             MEDIA_ROOT,
#             dirName,
#             localeTypeName,
#             inst.localeid,
#             ext)


class PlaceImages(models.Model):
    """Mapping between a place and its images."""

    image = models.ImageField(upload_to='places')
    place = models.ForeignKey(Place)
