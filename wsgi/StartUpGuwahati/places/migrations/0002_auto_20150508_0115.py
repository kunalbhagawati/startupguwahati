# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('city_name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('country_name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('locality_name', models.CharField(max_length=255)),
                ('latitude', models.DecimalField(max_digits=9, decimal_places=2, null=True)),
                ('longitude', models.DecimalField(max_digits=9, decimal_places=2, null=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='places.City')),
                ('parent_locality', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='places.Locality', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
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
        migrations.AddField(
            model_name='place',
            name='latitude',
            field=models.DecimalField(max_digits=9, decimal_places=2, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='place',
            name='locality',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='places.Locality'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='longitude',
            field=models.DecimalField(max_digits=9, decimal_places=2, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='place',
            name='street',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
    ]
