# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placefacilities',
            name='parent',
            field=models.ForeignKey(to='places.PlaceFacilities', null=True),
            preserve_default=True,
        ),
    ]
