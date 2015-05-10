"""Serializers for the homepage views and handler"""
__author__ = "Kunal Bhagawati"

# REST_FRAMEWORK
from rest_framework import serializers

# homepage module
from .models import *
from users import serializers as uSerializers
from users import (
    models as userModels,
    serializers as userSerializers)


class PlaceImagesSerializer(serializers.ModelSerializer):
    """Mapping between a place and its images."""

    class Meta:
        model = PlaceImages


class PublicPlaceAttributesSerializer(serializers.ModelSerializer):

    class Meta:
        model = PublicPlaceAttributes


class OwnerField(serializers.RelatedField):
    def to_representation(self, value):
        """Returns owner information name."""

        return userSerializers.UserSerializer(value).data

    def to_internal_value(self, data):
        """Inserts using ownerid."""

        # get locality
        return userModels.User.objects.get(pk=data)


class PrivatePlaceAttributesSerializer(serializers.ModelSerializer):

    owner = OwnerField(read_only=False, queryset=userModels.User.objects.all())

    class Meta:
        model = PrivatePlaceAttributes


class LocalityField(serializers.RelatedField):
    def to_representation(self, value):
        """Returns locality name."""

        return value.locality_name

    def to_internal_value(self, data):
        """Inserts using localityid."""

        # get locality
        return Locality.objects.get(pk=data)


class PlaceSerializer(serializers.ModelSerializer):
    """Serializers a place along with all its related fields."""

    privateplaceattributes = PrivatePlaceAttributesSerializer(read_only=True)
    publicplaceattributes = PublicPlaceAttributesSerializer(read_only=True)
    facilities = serializers.SlugRelatedField(
            many=True,
            read_only=False,
            slug_field='facility_name',
            queryset=PlaceFacilities.objects.all(),
         )
    placeimages_set = PlaceImagesSerializer(read_only=True, many=True)
    locality = LocalityField(read_only=False, queryset=Locality.objects.all())

    class Meta:
        model = Place
