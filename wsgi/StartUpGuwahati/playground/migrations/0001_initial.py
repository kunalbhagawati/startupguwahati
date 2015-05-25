# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dummy',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255, null=True)),
                ('createdon', models.DateTimeField(auto_now_add=True, null=True)),
                ('modifiedon', models.DateTimeField(null=True, auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
