# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('puzzles', '0003_remove_puzzle_games'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='puzzle',
            name='text',
        ),
        migrations.RemoveField(
            model_name='puzzleansweroption',
            name='image',
        ),
        migrations.AddField(
            model_name='puzzle',
            name='comparison_a_1',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='puzzle',
            name='comparison_a_2',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='puzzle',
            name='comparison_b_1',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='puzzle',
            name='comparison_b_2',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
