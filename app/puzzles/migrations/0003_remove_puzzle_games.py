# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('puzzles', '0002_puzzle_games'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='puzzle',
            name='games',
        ),
    ]
