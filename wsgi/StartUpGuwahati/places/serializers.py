"""Serializers for the homepage views and handler"""
__author__ = "Kunal Bhagawati"

# REST_FRAMEWORK
from rest_framework import serializers

# homepage module
from .models import *


class PlaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Place


# class MasterHomepagemoduleSerializer(serializers.ModelSerializer):

#     moduleid = serializers.IntegerField(read_only=True)
#     modulename = serializers.CharField(max_length=50, allow_blank=False)
#     inventorytype = serializers.ChoiceField(
#             allow_null=True,
#             choices=[('listing', 'listing'), ('user', 'user')],
#             required=False)
#     createdby = serializers.IntegerField(
#             max_value=2147483647,
#             min_value=-2147483648)
#     modifiedby = serializers.IntegerField(
#             max_value=2147483647,
#             min_value=-2147483648)
#     createdon = serializers.DateTimeField(
#             format="%Y-%m-%d %H:%M:%S",
#             read_only=True)
#     modifiedon = serializers.DateTimeField(
#             format="%Y-%m-%d %H:%M:%S",
#             read_only=True)
#     parentid = serializers.PrimaryKeyRelatedField(
#             allow_null=True,
#             queryset=MasterHomepagemodule.objects.all(),
#             required=False)

#     class Meta:
#         model = MasterHomepagemodule


# class MasterHomepagemoduleExtrafieldsSerializer(serializers.ModelSerializer):

#     fieldid = serializers.IntegerField(read_only=True)
#     fieldname = serializers.CharField(max_length=50, allow_blank=False)

#     class Meta:
#         model = MasterHomepagemoduleExtrafields


# class MappingHomepagemoduleExtrafieldsSerializer(serializers.ModelSerializer):

#     id = serializers.IntegerField(read_only=True)
#     moduleid = serializers.PrimaryKeyRelatedField(
#             queryset=MasterHomepagemodule.objects.all())
#     fieldid = serializers.SlugRelatedField(
#             queryset=MasterHomepagemoduleExtrafields.objects.all(),
#             slug_field='fieldname')
#     fieldvalue = serializers.CharField(max_length=200)
#     localeid = serializers.IntegerField(max_value=32767, min_value=-32768)
#     localetype = serializers.ChoiceField(choices=[(1, 'city'), (2, 'state')])

#     class Meta:
#         model = MappingHomepagemoduleExtrafields


# # -------------------------------------------------------------------


# class MappingHomepagemoduleInventorySerializer(
#         serializers.ModelSerializer):

#     id = serializers.IntegerField(read_only=True)
#     inventoryid = serializers.IntegerField(
#             max_value=2147483647,
#             min_value=-2147483648)
#     localeid = serializers.IntegerField(max_value=32767, min_value=-32768)
#     localetype = serializers.ChoiceField(
#             choices=[(1, 'city'), (2, 'state')])
#     startdate = serializers.DateField(
#             format="%Y-%m-%d",
#             allow_null=True,
#             required=False)
#     enddate = serializers.DateField(
#             format="%Y-%m-%d", allow_null=True, required=False)
#     createdby = serializers.IntegerField(max_value=2147483647,
#             min_value=-2147483648)
#     modifiedby = serializers.IntegerField(max_value=2147483647,
#             min_value=-2147483648)
#     createdon = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S",
#             read_only=True)
#     modifiedon = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S",
#             read_only=True)
#     status = serializers.BooleanField(default=1, required=False)
#     moduleid = serializers.PrimaryKeyRelatedField(
#             queryset=MasterHomepagemodule.objects.all())
#     extrafields = serializers.SerializerMethodField()

#     def get_extrafields(self, obj):
#         invRows = obj.mappinghomepagemoduleinventoryfields_set.all()
#         return dict([(i.fieldid.fieldname, i.fieldvalue) for i in invRows])

#     class Meta:
#         model = MappingHomepagemoduleInventory


# class MasterHomepagemoduleInventoryfieldsSerializer(
#         serializers.ModelSerializer):

#     fieldid = serializers.IntegerField(read_only=True)
#     fieldname = serializers.CharField(max_length=50, allow_blank=False)

#     class Meta:
#         model = MasterHomepagemoduleInventoryfields


# class MappingHomepagemoduleInventoryfieldsSerializer(
#         serializers.ModelSerializer):

#     id = serializers.IntegerField(read_only=True)
#     mappingrowid = serializers.PrimaryKeyRelatedField(
#             queryset=MappingHomepagemoduleInventory.objects.all())
#     fieldid = serializers.SlugRelatedField(
#             queryset=MasterHomepagemoduleInventoryfields.objects.all(),
#             slug_field='fieldname')
#     fieldvalue = serializers.CharField(max_length=200)

#     class Meta:
#         model = MappingHomepagemoduleInventoryfields


# class MasterHomepagemoduleInventoryfiltersSerializer(
#         serializers.ModelSerializer):

#     fieldid = serializers.IntegerField(read_only=True)
#     fieldname = serializers.CharField(max_length=50, allow_blank=False)

#     class Meta:
#         model = MasterHomepagemoduleInventoryfilters


# class MappingHomepagemoduleInventoryfiltersSerializer(
#         serializers.ModelSerializer):

#     id = serializers.IntegerField(read_only=True)
#     mappingrowid = serializers.PrimaryKeyRelatedField(
#             queryset=MappingHomepagemoduleInventory.objects.all())
#     fieldid = serializers.SlugRelatedField(
#             queryset=MasterHomepagemoduleInventoryfilters.objects.all(),
#             slug_field='fieldname')
#     fieldvalue = serializers.CharField(max_length=200)

#     class Meta:
#         model = MappingHomepagemoduleInventoryfilters


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
