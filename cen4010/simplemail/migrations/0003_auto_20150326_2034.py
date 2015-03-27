# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simplemail', '0002_auto_20150326_2017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='owned_emails',
            new_name='emails',
        ),
    ]
