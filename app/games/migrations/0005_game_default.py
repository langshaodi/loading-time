# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_auto_20151107_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='default',
            field=models.BooleanField(default=False),
        ),
    ]
