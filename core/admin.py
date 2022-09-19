
from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Snippet

admin.site.site_header = "Admin Tutorial Dashboard"

class SnippetAdmin(admin.ModelAdmin):
    exclude =  ('title',)
    fields = ('title',)

    
admin.site.register(Snippet,SnippetAdmin)
admin.site.unregister(Group)
# Register your models here.
