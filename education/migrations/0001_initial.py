# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('degree', models.CharField(max_length=500)),
                ('start_date', models.DateField(verbose_name=b'start date')),
                ('end_date', models.DateField(verbose_name=b'end date')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500)),
                ('location', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Universities',
            },
        ),
        migrations.AddField(
            model_name='education',
            name='school',
            field=models.ForeignKey(related_name='school', to='education.School'),
        ),
    ]
