# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('city_name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('country_name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('locality_name', models.CharField(max_length=255)),
                ('latitude', models.DecimalField(null=True, decimal_places=2, max_digits=9)),
                ('longitude', models.DecimalField(null=True, decimal_places=2, max_digits=9)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='places.City')),
                ('parent_locality', models.ForeignKey(to='places.Locality', on_delete=django.db.models.deletion.SET_NULL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlaceFacilities',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
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
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('place_name', models.CharField(max_length=50)),
                ('latitude', models.DecimalField(null=True, decimal_places=2, max_digits=9)),
                ('longitude', models.DecimalField(null=True, decimal_places=2, max_digits=9)),
                ('street', models.CharField(max_length=100, null=True)),
                ('is_place_covered', models.NullBooleanField()),
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
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('place_name', models.CharField(max_length=50)),
                ('latitude', models.DecimalField(null=True, decimal_places=2, max_digits=9)),
                ('longitude', models.DecimalField(null=True, decimal_places=2, max_digits=9)),
                ('street', models.CharField(max_length=100, null=True)),
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
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('state_name', models.CharField(max_length=255)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='places.Country')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='places.State'),
            preserve_default=True,
        ),
    ]
