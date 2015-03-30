# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simplemail', '0006_remove_userprofile_emails'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='inbox',
            field=models.ManyToManyField(related_name='inbox_users', to='simplemail.Email'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='outbox',
            field=models.ManyToManyField(related_name='outbox_users', to='simplemail.Email'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='trash',
            field=models.ManyToManyField(related_name='trash_users', to='simplemail.Email'),
            preserve_default=True,
        ),
    ]
