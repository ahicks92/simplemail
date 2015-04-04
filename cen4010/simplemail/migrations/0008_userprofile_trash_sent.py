# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simplemail', '0007_auto_20150330_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='trash_sent',
            field=models.ManyToManyField(related_name='trash_sent_users', to='simplemail.Email'),
            preserve_default=True,
        ),
    ]
