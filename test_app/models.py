from django.db import models
from django.conf import settings
# Create your models here.


class UserProfile(models.Model):
    name = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='user_profile', null=True, blank=True)
    id = models.IntegerField(primary_key=True, help_text='user UID as the primary key in our database')
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,
                              null=True, blank=True)
    access_token = models.CharField('Access Token', max_length=200, null=True, blank=True,
    help_text='opaque string that identifies a user, app, or page .')

    def __str__(self):
        return "%s with access token as %s" % (self.name, self.access_token)