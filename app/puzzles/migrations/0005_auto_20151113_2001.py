# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('puzzles', '0004_auto_20151113_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puzzle',
            name='comparison_a_1',
            field=models.CharField(help_text=b'A:B::X:Y', max_length=50, null=True, verbose_name=b'A', blank=True),
        ),
        migrations.AlterField(
            model_name='puzzle',
            name='comparison_a_2',
            field=models.CharField(help_text=b'A:B::X:Y', max_length=50, null=True, verbose_name=b'B', blank=True),
        ),
        migrations.AlterField(
            model_name='puzzle',
            name='comparison_b_1',
            field=models.CharField(help_text=b'A:B::X:Y', max_length=50, null=True, verbose_name=b'X', blank=True),
        ),
        migrations.AlterField(
            model_name='puzzle',
            name='comparison_b_2',
            field=models.CharField(help_text=b'A:B::X:Y', max_length=50, null=True, verbose_name=b'Y', blank=True),
        ),
    ]
