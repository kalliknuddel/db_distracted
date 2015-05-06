# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actor_id', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('sort_order', models.IntegerField()),
                ('image', models.URLField()),
                ('actor', models.ForeignKey(to='distracted.Actor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('series_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('alias', models.CharField(max_length=100)),
                ('overview', models.CharField(max_length=400)),
                ('banner', models.URLField()),
                ('first_aired', models.DateField(verbose_name=b'FirstAired')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='roles',
            name='series',
            field=models.ForeignKey(to='distracted.Series'),
            preserve_default=True,
        ),
    ]
