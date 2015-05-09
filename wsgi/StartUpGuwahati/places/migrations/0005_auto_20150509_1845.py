# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_auto_20150509_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locality',
            name='latitude',
            field=models.DecimalField(max_digits=9, null=True, decimal_places=7),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='locality',
            name='longitude',
            field=models.DecimalField(max_digits=9, null=True, decimal_places=7),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='place',
            name='latitude',
            field=models.DecimalField(max_digits=9, null=True, decimal_places=7),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='place',
            name='longitude',
            field=models.DecimalField(max_digits=9, null=True, decimal_places=7),
            preserve_default=True,
        ),
    ]
