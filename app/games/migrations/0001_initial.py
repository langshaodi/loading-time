# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import games.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('delay', models.BigIntegerField(default=games.models.random_timeout)),
            ],
        ),
    ]
