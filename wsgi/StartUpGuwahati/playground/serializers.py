# REST_FRAMEWORK
from rest_framework import serializers

# playground module
from .models import *


class DummySerializer(serializers.ModelSerializer):
    """Dummy Serializer."""

    class Meta:
        model = Dummy
