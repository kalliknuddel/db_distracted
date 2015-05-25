# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('distracted', '0007_auto_20150512_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='firstAired',
            field=models.DateField(blank=True, verbose_name='FirstAired', null=True),
            preserve_default=True,
        ),
    ]
