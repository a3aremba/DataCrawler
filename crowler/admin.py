from django.contrib import admin
from crowler.models import *

class RelevantWordsAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'word', 'tag_history')
    
admin.site.register(RelevantWords, RelevantWordsAdmin)