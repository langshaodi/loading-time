# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('puzzles', '0003_remove_puzzle_games'),
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='puzzles',
            field=models.ManyToManyField(to='puzzles.Puzzle'),
        ),
    ]
