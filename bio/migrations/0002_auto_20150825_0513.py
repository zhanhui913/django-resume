# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Biography',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=2000)),
                ('email', models.EmailField(max_length=254)),
                ('github', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=5000, blank=True)),
                ('start_date', models.DateField(verbose_name=b'start date')),
                ('end_date', models.DateField(verbose_name=b'end date', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.AlterField(
            model_name='company',
            name='location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='education',
            name='degree',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='education',
            name='end_date',
            field=models.DateField(verbose_name=b'end date', blank=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='major',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='employment',
            name='end_date',
            field=models.DateField(verbose_name=b'end date', blank=True),
        ),
        migrations.AlterField(
            model_name='employment',
            name='position',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='school',
            name='location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
