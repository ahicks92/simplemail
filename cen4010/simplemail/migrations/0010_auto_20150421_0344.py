# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simplemail', '0009_email_to_addresses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='signature',
            field=models.TextField(default=b''),
        ),
    ]
