# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='major',
            field=models.CharField(max_length=500, blank=True),
        ),
    ]
