from django.contrib import admin
from .models import UserProfile
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'access_token']
    list_filter = ['name', 'id']


admin.site.register(UserProfile, UserProfileAdmin)
