# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_auto_20150509_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='description',
            field=models.CharField(null=True, max_length=255),
            preserve_default=True,
        ),
    ]
