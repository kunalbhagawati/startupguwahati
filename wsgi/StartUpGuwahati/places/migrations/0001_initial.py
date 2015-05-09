# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('city_name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('country_name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('locality_name', models.CharField(max_length=255)),
                ('latitude', models.DecimalField(decimal_places=2, max_digits=9, null=True)),
                ('longitude', models.DecimalField(decimal_places=2, max_digits=9, null=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='places.City')),
                ('parent_locality', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='places.Locality')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('place_name', models.CharField(max_length=50)),
                ('latitude', models.DecimalField(decimal_places=2, max_digits=9, null=True)),
                ('longitude', models.DecimalField(decimal_places=2, max_digits=9, null=True)),
                ('street', models.CharField(null=True, max_length=100)),
                ('is_place_covered', models.NullBooleanField()),
                ('is_place_private', models.BooleanField(default=True)),
                ('createdon', models.DateTimeField(auto_now_add=True, null=True)),
                ('modifiedon', models.DateTimeField(null=True, auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlaceFacilities',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('facility_name', models.CharField(max_length=100)),
                ('parent', models.ForeignKey(to='places.PlaceFacilities')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlaceImages',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('owner', models.ForeignKey(to='users.User')),
                ('place', models.ForeignKey(to='places.Place')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PublicPlaceAttributes',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('place_type', models.IntegerField(choices=[(1, 'Hangout Spot'), (2, 'Free')])),
                ('place', models.ForeignKey(to='places.Place')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('state_name', models.CharField(max_length=255)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='places.Country')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='place',
            name='facilities',
            field=models.ManyToManyField(to='places.PlaceFacilities'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='place',
            name='locality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='places.Locality'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='places.State'),
            preserve_default=True,
        ),
    ]
