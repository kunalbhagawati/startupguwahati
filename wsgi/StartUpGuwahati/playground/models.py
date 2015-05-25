from django.db import models


class Dummy(models.Model):
    """Dummy model."""

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, null=True)
    createdon = models.DateTimeField(auto_now_add=True, null=True)
    modifiedon = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name
