# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simplemail', '0004_auto_20150326_2035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='was_sent',
        ),
    ]
