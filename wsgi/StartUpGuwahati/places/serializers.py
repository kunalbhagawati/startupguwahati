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
    placeimages_set = serializers.PlaceImagesSerializer(read_only=True)

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
        fields = ('place_name', 'latitude', 'longitude', 'street', 'locality',
                'is_covered', 'is_private', 'createdon', 'modifiedon',
                'placeimages_set', 'privateplaceattributes',
                'publicplaceattributes', 'facilities',)


# class MappingHomepagebannerLocaleSerializer(serializers.ModelSerializer):
#     """Serializes the homepage banners."""

#     id = serializers.IntegerField(label='ID', read_only=True)
#     banner = serializers.ImageField(max_length=100, use_url=True)
#     localeid = serializers.IntegerField(
#                 max_value=2147483647, min_value=-2147483648, required=True)
#     localetype = serializers.ChoiceField(
#                 choices=[
#                     (1, 'city'),
#                     (2, 'state')],
#                 required=True)

#     class Meta:
#         model = MappingHomepagebannerLocale
#         # validators = [
#         #         serializers.UniqueTogetherValidator(
#         #             queryset=MappingHomepagebannerLocale.objects.all(),
#         #             fields=('localeid', 'localetype'))]
