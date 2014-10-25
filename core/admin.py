from django.contrib import admin
from core.models import *

class SiteConfigAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'name', 'html_content', 'date')
    
admin.site.register(SiteConfig, SiteConfigAdmin)