# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='Duty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('task', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.CharField(max_length=200)),
                ('start_date', models.DateField(verbose_name=b'start date')),
                ('end_date', models.DateField(verbose_name=b'end date')),
                ('company', models.ForeignKey(related_name='employment', to='employment.Company')),
            ],
        ),
        migrations.AddField(
            model_name='duty',
            name='employment',
            field=models.ForeignKey(related_name='duty', to='employment.Employment'),
        ),
    ]
