# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simplemail', '0005_remove_email_was_sent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='emails',
        ),
    ]
