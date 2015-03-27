# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simplemail', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='body_stripped',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='email',
            name='signature',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
