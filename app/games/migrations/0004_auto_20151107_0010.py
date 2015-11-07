# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_auto_20151105_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='puzzles',
            field=models.ManyToManyField(to='puzzles.Puzzle'),
        ),
    ]
