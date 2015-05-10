"""Serializers for the homepage views and handler"""
__author__ = "Kunal Bhagawati"

# REST_FRAMEWORK
from rest_framework import serializers

# homepage module
from .models import *
from users import serializers as uSerializers


class PlaceImagesSerializer(serializers.ModelSerializer):
    """Mapping between a place and its images."""

    class Meta:
        model = PlaceImages


class PublicPlaceAttributesSerializer(serializers.ModelSerializer):

    class Meta:
        model = PublicPlaceAttributes


class PrivatePlaceAttributesSerializer(serializers.ModelSerializer):

    owner = uSerializers.UserSerializer(read_only=True)

    class Meta:
        model = PrivatePlaceAttributes


class PrivatePlaceAttributesCreationSerializer(serializers.ModelSerializer):

    place = serializers.PrimaryKeyRelatedField(queryset=Place.objects.all())

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

    # def get_attributes(self, obj):
    #     # if obj.is_private:
    #     #     pType = private
    #     # else:
    #     #     pType = public

    #     # if hasattr(obj, '{0}placeattributes'.format(pType)):
    #     #     return dict
    #     # else:
    #     #     return None

    #     if obj.is_private:
    #         if hasattr(obj, 'privateplaceattributes'):
    #             return {
    #                 'owner': (uSerializers
    #                     .UserSerializer(obj.privateplaceattributes.owner)
    #                     .data)
    #                 }
    #     else:
    #         if hasattr(obj, 'publicplaceattributes'):
    #             return {
    #                 'place_type': obj.publicplaceattributes.place_type
    #                 }

    #     return None

    # def create(self, validated_data):
    #     profile_data = validated_data.pop('profile')
    #     user = User.objects.create(**validated_data)
    #     Profile.objects.create(user=user, **profile_data)
    #     return user

    class Meta:
        model = Place
