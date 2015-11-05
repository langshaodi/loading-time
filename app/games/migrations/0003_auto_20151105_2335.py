# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_game_puzzles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='puzzles',
            field=models.ManyToManyField(to='puzzles.Puzzle', null=True, blank=True),
        ),
    ]
