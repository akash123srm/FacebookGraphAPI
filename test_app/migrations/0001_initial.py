# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.IntegerField(help_text=b'user UID as the primary key in our database', serialize=False, primary_key=True)),
                ('image', models.ImageField(null=True, upload_to=None, blank=True)),
                ('access_token', models.CharField(help_text=b'opaque string that identifies a user, app, or page .', max_length=200, null=True, verbose_name=b'Access Token', blank=True)),
                ('name', models.OneToOneField(related_name='user_profile', null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
