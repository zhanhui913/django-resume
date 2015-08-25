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
            options={
                'verbose_name_plural': 'Duties',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('degree', models.CharField(max_length=500)),
                ('major', models.CharField(max_length=500, blank=True)),
                ('start_date', models.DateField(verbose_name=b'start date')),
                ('end_date', models.DateField(verbose_name=b'end date')),
            ],
        ),
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.CharField(max_length=200)),
                ('start_date', models.DateField(verbose_name=b'start date')),
                ('end_date', models.DateField(verbose_name=b'end date')),
                ('company', models.ForeignKey(related_name='employment', to='bio.Company')),
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
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Skills',
            },
        ),
        migrations.AddField(
            model_name='education',
            name='school',
            field=models.ForeignKey(related_name='school', to='bio.School'),
        ),
        migrations.AddField(
            model_name='duty',
            name='employment',
            field=models.ForeignKey(related_name='duty', to='bio.Employment'),
        ),
    ]
