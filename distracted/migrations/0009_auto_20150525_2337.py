# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('distracted', '0008_auto_20150525_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='series_id',
            field=models.IntegerField(unique=True),
            preserve_default=True,
        ),
    ]
