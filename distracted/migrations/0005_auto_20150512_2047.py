# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('distracted', '0004_auto_20150512_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='overview',
            field=models.CharField(max_length=1000),
            preserve_default=True,
        ),
    ]
