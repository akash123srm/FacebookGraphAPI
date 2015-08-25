# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='image',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_id',
            field=models.IntegerField(default=1, help_text=b'user UID as the primary key in our database'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='access_token',
            field=models.CharField(default=None, help_text=b'opaque string that identifies a user, app, or page .', max_length=200, verbose_name=b'Access Token'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.OneToOneField(related_name='user_profile', default=None, to=settings.AUTH_USER_MODEL),
        ),
    ]
