# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simplemail', '0008_userprofile_trash_sent'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='to_addresses',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
