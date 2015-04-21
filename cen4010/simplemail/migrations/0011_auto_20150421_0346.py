# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simplemail', '0010_auto_20150421_0344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='signature',
            field=models.TextField(default=b''),
        ),
    ]
