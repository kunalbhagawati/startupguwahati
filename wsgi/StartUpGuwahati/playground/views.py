# # django core
from django.contrib.auth.models import User

# # REST Framework
from rest_framework import generics

# Auth
from rest_framework.authentication import (
        SessionAuthentication,
        BasicAuthentication,
        TokenAuthentication)

from rest_framework.permissions import (
        IsAuthenticated,
        IsAuthenticatedOrReadOnly)

from . import models, serializers


class DummyList(generics.ListCreateAPIView):

    queryset = models.Dummy.objects.all()
    serializer_class = serializers.DummySerializer
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    paginate_by = 10


class GetUpdateDeleteDummyView(generics.RetrieveUpdateDestroyAPIView):

    queryset = models.Dummy.objects.all()
    serializer_class = serializers.DummySerializer
    # permission_classes = (IsAuthenticated,)
    paginate_by = 10
