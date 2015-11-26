# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('responses', '0003_auto_20151126_0515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameresponse',
            name='game',
            field=models.ForeignKey(to='games.Game'),
        ),
    ]
