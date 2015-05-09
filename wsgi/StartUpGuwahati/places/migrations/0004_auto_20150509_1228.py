# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_auto_20150509_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='is_place_private',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
