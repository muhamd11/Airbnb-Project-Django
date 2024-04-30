from django.contrib import admin
from .models import About, FAQ

# Register your models here.

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('what_we_do', 'our_mission', 'our_goals', 'image', )
    
@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', )
        