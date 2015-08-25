# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0003_auto_20150825_0517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biography',
            name='github',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='end_date',
            field=models.DateField(null=True, verbose_name=b'end date', blank=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='major',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employment',
            name='end_date',
            field=models.DateField(null=True, verbose_name=b'end date', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(default=datetime.datetime(2015, 8, 25, 5, 25, 19, 266331, tzinfo=utc), max_length=5000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateField(null=True, verbose_name=b'end date', blank=True),
        ),
    ]
