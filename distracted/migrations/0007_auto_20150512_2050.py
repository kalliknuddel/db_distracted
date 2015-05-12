# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('distracted', '0006_auto_20150512_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='seasonNumber',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
