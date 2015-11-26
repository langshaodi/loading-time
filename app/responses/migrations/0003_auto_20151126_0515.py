# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('responses', '0002_auto_20151105_2357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='response',
            name='name',
        ),
        migrations.AddField(
            model_name='response',
            name='submitted',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 26, 5, 15, 28, 259225, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
