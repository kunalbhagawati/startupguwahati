# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('places', '0002_privateplace_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('place_name', models.CharField(max_length=50)),
                ('latitude', models.DecimalField(null=True, max_digits=9, decimal_places=2)),
                ('longitude', models.DecimalField(null=True, max_digits=9, decimal_places=2)),
                ('street', models.CharField(max_length=100, null=True)),
                ('is_place_covered', models.NullBooleanField()),
                ('is_place_private', models.BooleanField()),
                ('facilities', models.ManyToManyField(to='places.PlaceFacilities')),
                ('locality', models.ForeignKey(to='places.Locality', on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlaceAttributes',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlaceImages',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('image', models.ImageField(upload_to='places')),
                ('place', models.ForeignKey(to='places.Place')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PrivatePlaceAttributes',
            fields=[
                ('placeattributes_ptr', models.OneToOneField(primary_key=True, to='places.PlaceAttributes', auto_created=True, serialize=False, parent_link=True)),
                ('owner', models.ForeignKey(to='users.User')),
                ('place', models.ForeignKey(to='places.Place')),
            ],
            options={
            },
            bases=('places.placeattributes',),
        ),
        migrations.CreateModel(
            name='PublicPlaceAttributes',
            fields=[
                ('placeattributes_ptr', models.OneToOneField(primary_key=True, to='places.PlaceAttributes', auto_created=True, serialize=False, parent_link=True)),
                ('place_type', models.IntegerField(choices=[(1, 'Hangout Spot'), (2, 'Free')])),
                ('place', models.ForeignKey(to='places.Place')),
            ],
            options={
            },
            bases=('places.placeattributes',),
        ),
        migrations.RemoveField(
            model_name='privateplace',
            name='facilities',
        ),
        migrations.RemoveField(
            model_name='privateplace',
            name='locality',
        ),
        migrations.RemoveField(
            model_name='privateplace',
            name='owner',
        ),
        migrations.DeleteModel(
            name='PrivatePlace',
        ),
        migrations.RemoveField(
            model_name='publicplace',
            name='facilities',
        ),
        migrations.RemoveField(
            model_name='publicplace',
            name='locality',
        ),
        migrations.DeleteModel(
            name='PublicPlace',
        ),
    ]
