# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('distracted', '0005_auto_20150512_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='overview',
            field=models.CharField(max_length=1500),
            preserve_default=True,
        ),
    ]
