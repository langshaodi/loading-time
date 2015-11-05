# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Puzzle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='PuzzleAnswerOption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('correct', models.BooleanField(default=False)),
                ('text', models.CharField(max_length=500, null=True, blank=True)),
                ('image', models.FileField(null=True, upload_to=b'media/', blank=True)),
                ('puzzle', models.ForeignKey(to='puzzles.Puzzle')),
            ],
        ),
    ]
