# # core
import json

# # Third Party
import django_filters

# # REST Framework
from rest_framework import generics

# # App
from . import models, serializers


class UserFilter(django_filters.FilterSet):

    class Meta:
        model = models.User
        fields = {
            'username': ['exact'],
            'name': ['iexact'],
            'email': ['exact'],
            }


class UserList(generics.ListCreateAPIView):
    """List all users or create a new one."""

    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    paginate_by = 10
    filter_class = UserFilter
    search_fields = ('username', 'email')


class UserUpdate(generics.RetrieveUpdateDestroyAPIView):
    """Get a particular user and/or update/delete it."""

    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
