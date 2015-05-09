from django.db import models


# TODO change to django user model
class User(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=20)
    email = models.EmailField()
