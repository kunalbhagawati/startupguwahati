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
            # 'magnification': ['exact', 'lte', 'lt', 'gte', 'gt'],
            # 'field_of_view': ['exact', 'lte', 'lt', 'gte', 'gt'],
            # 'view_range': ['exact', 'lte', 'lt', 'gte', 'gt'],
            }


class PlacesList(generics.ListAPIView):
    """List all devices or create a new one."""

    queryset = models.Place.objects.all()
    serializer_class = serializers.PlaceSerializer
    # permission_classes = (IsAdminUser,)
    paginate_by = 10
    filter_class = PlaceFilter
    search_fields = ('place_name', )

    # def perform_create(self, serializer):
    #     dObj = serializer.save()
    #     dObjSerialized = serializers.DeviceSerializer(dObj).data
    #     rConn.hset(hashName, dObj.pk, json.dumps(dObjSerialized))


# class DeviceUpdate(generics.RetrieveUpdateDestroyAPIView):
#     """Get a particular device and/or update/delete it."""

#     queryset = models.Device.objects.all()
#     serializer_class = serializers.DeviceSerializer
#     permission_classes = (IsAdminUser,)

#     def get(self, request, *args, **kwargs):
#         device = rConn.hget(hashName, kwargs['pk'])
#         if device:
#             device = RedisConverter.decode(device)
#             return Response(json.loads(device), status=200)
#         res = self.retrieve(request, *args, **kwargs)
#         rConn.hset(hashName, kwargs['pk'], json.dumps(res.data))
#         return res

#     def perform_update(self, serializer):
#         dObj = serializer.save()
#         dObjSerialized = serializers.DeviceSerializer(dObj).data
#         rConn.hset(hashName, dObj.pk, json.dumps(dObjSerialized))

#     def perform_destroy(self, instance):
#         dId = instance.pk
#         instance.delete()
#         rConn.hdel(hashName, dId)
