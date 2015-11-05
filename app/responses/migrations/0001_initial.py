# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_auto_20151105_2335'),
        ('puzzles', '0003_remove_puzzle_games'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameResponse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('submitted', models.DateTimeField(auto_now=True)),
                ('frustration', models.SmallIntegerField()),
                ('total_time', models.FloatField(null=True, blank=True)),
                ('game', models.OneToOneField(to='games.Game')),
            ],
        ),
        migrations.CreateModel(
            name='PuzzleResponse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.FloatField()),
                ('answer', models.ForeignKey(to='puzzles.PuzzleAnswerOption')),
                ('game_response', models.ForeignKey(to='responses.GameResponse')),
                ('puzzle', models.ForeignKey(to='puzzles.Puzzle')),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='gameresponse',
            name='response',
            field=models.ForeignKey(to='responses.Response'),
        ),
    ]
