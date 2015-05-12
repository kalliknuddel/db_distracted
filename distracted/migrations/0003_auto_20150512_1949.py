# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('distracted', '0002_auto_20150512_1511'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('director', models.CharField(max_length=100)),
                ('episodeName', models.CharField(max_length=100)),
                ('firstAired', models.DateField(verbose_name='FirstAired')),
                ('rating', models.CharField(max_length=100)),
                ('voters', models.CharField(max_length=100)),
                ('episodeNumber', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('season_id', models.IntegerField(serialize=False, primary_key=True)),
                ('seasonNumber', models.IntegerField(unique=True)),
                ('series_id', models.ForeignKey(to='distracted.Series', on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='episode',
            name='season_id',
            field=models.ForeignKey(to='distracted.Season', on_delete=django.db.models.deletion.PROTECT),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='episode',
            name='series_id',
            field=models.ForeignKey(to='distracted.Series', on_delete=django.db.models.deletion.PROTECT),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='series',
            name='alias',
        ),
    ]
