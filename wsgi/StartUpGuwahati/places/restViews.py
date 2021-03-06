# # core
import json
from decimal import Decimal

# # Third Party
import django_filters

from django.db import transaction

# # REST Framework
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
# from rest_framework.permissions import IsAdminUser

# # App
from . import models, serializers


class PlaceFilter(django_filters.FilterSet):

    class Meta:
        model = models.Place
        fields = {
            'place_name': ['iexact'],
            'locality': ['exact'],
            'locality__city': ['exact'],
            'is_covered': ['exact'],
            'is_private': ['exact'],
            }


class PlaceList(generics.ListCreateAPIView):
    """List all places or create a new one."""

    queryset = models.Place.objects.all()
    serializer_class = serializers.PlaceSerializer
    # permission_classes = (IsAdminUser,)
    paginate_by = 10
    filter_class = PlaceFilter
    search_fields = ('place_name', )

    def perform_create(self, serializer):
        """Saves the owner or the property type, as per the request."""

        try:
            with transaction.atomic():
                placeObj = serializer.save()

                if placeObj.is_private:
                    attrType = 'privateplaceattributes'
                    prvAttr = self.request.data.pop(attrType)
                    prvAttr['place'] = placeObj.pk
                    ser = serializers.PrivatePlaceAttributesSerializer(
                            data=prvAttr)
                else:
                    attrType = 'publicplaceattributes'
                    pubAttr = self.request.data.pop(attrType)
                    pubAttr['place'] = placeObj.pk
                    ser = serializers.PublicPlaceAttributesSerializer(
                            data=pubAttr)

                if ser.is_valid():
                    ser.save()
                else:
                    raise Exception({attrType: ser.errors})
        except:
            raise


class PlaceUpdate(generics.RetrieveUpdateDestroyAPIView):
    """Get a particular place and/or update/delete it."""

    queryset = models.Place.objects.all()
    serializer_class = serializers.PlaceSerializer
    # permission_classes = (IsAdminUser,)

    def perform_update(self, serializer):
        try:
            with transaction.atomic():
                placeObj = serializer.save()

                if placeObj.is_private:
                    attrType = 'privateplaceattributes'
                    prvAttr = self.request.data.pop(attrType)
                    prvAttr['place'] = placeObj.pk
                    ser = serializers.PrivatePlaceAttributesCreationSerializer(
                            placeObj.privateplaceattributes,
                            data=prvAttr)
                else:
                    attrType = 'publicplaceattributes'
                    pubAttr = self.request.data.pop(attrType)
                    pubAttr['place'] = placeObj.pk
                    ser = serializers.PublicPlaceAttributesSerializer(
                            placeObj.publicplaceattributes,
                            data=pubAttr)

                if ser.is_valid():
                    ser.save()
                else:
                    raise Exception({attrType: ser.errors})
        except:
            raise


class PlaceImagesCreate(generics.ListCreateAPIView):

    serializer_class = serializers.PlaceImagesSerializer

    def get_queryset(self):
        return models.PlaceImages.objects.filter(place=self.kwargs['pk'])


class PlaceImagesUpdate(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = serializers.PlaceImagesSerializer
    lookup_url_kwarg = 'imgId'

    def get_queryset(self):
        return models.PlaceImages.objects.filter(
                place=self.kwargs['pk'],
                pk=self.kwargs['imgId'])


class GetNearbyPlacesByLatLongView(APIView):
    """Gets the nearby places for a given lat long."""

    def get(self, request):
        qp = request.query_params
        if not qp.get('latitude', None) or not qp.get('longitude', None):
            return Response("No latitude or longitude passed to "
                    "search nearby places.", status=400)

        radius = int(qp.get('radius', 2))
        places = models.get_places_nearby(
                (Decimal(qp['latitude']), Decimal(qp['longitude'])),
                radius=radius)
        res = serializers.PlaceSerializer(places, many=True)
        return Response(res.data, status=200)


class GetNearbyPlacesForModel(APIView):
    """Gets the nearby places for a given model."""

    def get(self, request, pk):
        try:
            place = models.Place.objects.get(pk=pk)
        except models.Place.DoesNotExist:
            return Response("Place with id {0} does not exist."
                    .format(pk),
                    status=400)

        qp = request.query_params

        radius = int(qp.get('radius', 2))
        places = place.get_places_nearby(radius=radius)
        res = serializers.PlaceSerializer(places, many=True)
        return Response(res.data, status=200)
