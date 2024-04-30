from django.contrib import admin
from . models import Settings
# Register your models here.

@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'phone', 'logo', 'email', 'address', 'description', 'facebook_link', 'twitter_link', 'instagram_link')
    