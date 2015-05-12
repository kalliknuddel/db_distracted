# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('distracted', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='lastUpdate',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='series',
            name='network',
            field=models.CharField(default='', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='series',
            name='rating',
            field=models.CharField(default='0.0', max_length=10),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='series',
            name='runtime',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='series',
            name='status',
            field=models.CharField(choices=[('running', 'Running'), ('discontinued', 'Discontinued')], default='running', max_length=15),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='series',
            name='voters',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='roles',
            name='actor',
            field=models.ForeignKey(to='distracted.Actor', on_delete=django.db.models.deletion.PROTECT),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='roles',
            name='series',
            field=models.ForeignKey(to='distracted.Series', on_delete=django.db.models.deletion.PROTECT),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='series',
            name='first_aired',
            field=models.DateField(verbose_name='FirstAired'),
            preserve_default=True,
        ),
    ]
