"""Serializers for the homepage views and handler"""
__author__ = "Kunal Bhagawati"

# REST_FRAMEWORK
from rest_framework import serializers

# homepage module
from .models import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
