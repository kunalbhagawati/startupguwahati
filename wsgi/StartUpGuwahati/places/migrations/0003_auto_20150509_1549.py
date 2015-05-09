# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_auto_20150509_1536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='privateplaceattributes',
            name='id',
        ),
        migrations.RemoveField(
            model_name='publicplaceattributes',
            name='id',
        ),
        migrations.AlterField(
            model_name='privateplaceattributes',
            name='place',
            field=models.OneToOneField(to='places.Place', serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicplaceattributes',
            name='place',
            field=models.OneToOneField(to='places.Place', serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
