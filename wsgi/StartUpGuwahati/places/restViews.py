# # core
import json

# # Third Party
import django_filters

# # REST Framework
from rest_framework.response import Response
from rest_framework import generics
# from rest_framework.permissions import IsAdminUser

# # App
from . import models, serializers


class PlaceFilter(django_filters.FilterSet):

    class Meta:
        model = models.Place
        fields = {
            'place_name': ['exact'],
            'locality': ['exact'],
            'locality__city': ['exact'],
            'is_covered': ['exact'],
            'is_private': ['exact'],
            }


class PlacesList(generics.ListCreateAPIView):
    """List all places or create a new one."""

    queryset = models.Place.objects.all()
    serializer_class = serializers.PlaceSerializer
    # permission_classes = (IsAdminUser,)
    paginate_by = 10
    filter_class = PlaceFilter
    search_fields = ('place_name', )

    def perform_create(self, serializer):
        """Saves the owner or the property type, as per the request."""

        # first remove the
        # serializer.data.pop()
        pass

        # placeObj = serializer.save()
        # placeObjSerialized = serializers.PlaceSerializer(placeObj).data
        # rConn.hset(hashName, placeObj.pk, json.dumps(dObjSerialized))


class PlaceUpdate(generics.RetrieveUpdateDestroyAPIView):
    """Get a particular place and/or update/delete it."""

    queryset = models.Place.objects.all()
    serializer_class = serializers.PlaceSerializer
    # permission_classes = (IsAdminUser,)

    # def get(self, request, *args, **kwargs):
    #     device = rConn.hget(hashName, kwargs['pk'])
    #     if device:
    #         device = RedisConverter.decode(device)
    #         return Response(json.loads(device), status=200)
    #     res = self.retrieve(request, *args, **kwargs)
    #     rConn.hset(hashName, kwargs['pk'], json.dumps(res.data))
    #     return res

    # def perform_update(self, serializer):
    #     dObj = serializer.save()
    #     dObjSerialized = serializers.DeviceSerializer(dObj).data
    #     rConn.hset(hashName, dObj.pk, json.dumps(dObjSerialized))

    # def perform_destroy(self, instance):
    #     dId = instance.pk
    #     instance.delete()
    #     rConn.hdel(hashName, dId)


class PlaceImagesCreate(generics.ListCreateAPIView):

    queryset = models.PlaceImages.objects.all()
    serializer_class = serializers.PlaceImagesSerializer


class PlaceImagesUpdate(generics.RetrieveUpdateDestroyAPIView):

    queryset = models.PlaceImages.objects.all()
    serializer_class = serializers.PlaceImagesSerializer
