# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('distracted', '0003_auto_20150512_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='season_id',
            field=models.ForeignKey(to='distracted.Season'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='episode',
            name='series_id',
            field=models.ForeignKey(to='distracted.Series'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='roles',
            name='actor',
            field=models.ForeignKey(to='distracted.Actor'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='roles',
            name='series',
            field=models.ForeignKey(to='distracted.Series'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='season',
            name='series_id',
            field=models.ForeignKey(to='distracted.Series'),
            preserve_default=True,
        ),
    ]
