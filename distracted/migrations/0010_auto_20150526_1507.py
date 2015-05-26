# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('distracted', '0009_auto_20150525_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='status',
            field=models.CharField(default='RUNNING', max_length=15, choices=[('running', 'Running'), ('discontinued', 'Discontinued')]),
            preserve_default=True,
        ),
    ]
