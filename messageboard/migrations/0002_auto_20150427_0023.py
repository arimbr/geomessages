# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messageboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='geomessage',
            old_name='point',
            new_name='location',
        ),
    ]
