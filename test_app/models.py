from django.db import models
from django.conf import settings
# Create your models here.


class UserProfile(models.Model):
    name = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='user_profile',default=None)
    user_id = models.IntegerField(help_text='user UID as the primary key in our database',default=1)
    access_token = models.CharField('Access Token', max_length=200,
    help_text='opaque string that identifies a user, app, or page .',default=None)

    def __str__(self):
        return "%s with access token as %s" % (self.name, self.access_token)