# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_auto_20150509_1549'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='is_place_covered',
            new_name='is_covered',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='is_place_private',
            new_name='is_private',
        ),
    ]
