# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simplemail', '0011_auto_20150421_0346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='mailgun_json',
        ),
    ]
