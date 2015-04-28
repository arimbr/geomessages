# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('messageboard', '0002_auto_20150427_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='geomessage',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 28, 10, 33, 56, 419341, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
