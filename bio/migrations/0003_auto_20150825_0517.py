# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0002_auto_20150825_0513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biography',
            name='github',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='end_date',
            field=models.DateField(null=True, verbose_name=b'end date'),
        ),
        migrations.AlterField(
            model_name='education',
            name='major',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employment',
            name='end_date',
            field=models.DateField(null=True, verbose_name=b'end date'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateField(null=True, verbose_name=b'end date'),
        ),
    ]
