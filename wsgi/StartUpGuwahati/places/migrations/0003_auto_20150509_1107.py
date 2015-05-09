# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_auto_20150508_0115'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceFacilities',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('facility_name', models.CharField(max_length=100)),
                ('parent', models.ForeignKey(to='places.PlaceFacilities')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PrivatePlace',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=50)),
                ('latitude', models.DecimalField(null=True, max_digits=9, decimal_places=2)),
                ('longitude', models.DecimalField(null=True, max_digits=9, decimal_places=2)),
                ('street', models.CharField(null=True, max_length=100)),
                ('is_place_covered', models.NullBooleanField()),
                ('owner', models.IntegerField()),
                ('facilities', models.ManyToManyField(to='places.PlaceFacilities')),
                ('locality', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='places.Locality')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PublicPlace',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=50)),
                ('latitude', models.DecimalField(null=True, max_digits=9, decimal_places=2)),
                ('longitude', models.DecimalField(null=True, max_digits=9, decimal_places=2)),
                ('street', models.CharField(null=True, max_length=100)),
                ('is_place_covered', models.NullBooleanField()),
                ('place_type', models.IntegerField(choices=[(1, 'Hangout Spot'), (2, 'Free')])),
                ('facilities', models.ManyToManyField(to='places.PlaceFacilities')),
                ('locality', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='places.Locality')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='place',
            name='locality',
        ),
        migrations.DeleteModel(
            name='Place',
        ),
    ]
