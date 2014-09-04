from django.contrib import admin
from sources.models import Source


class SourceAdmin(admin.ModelAdmin):
    list_display = ('source_url', 'gender', 'location')

admin.site.register(Source, SourceAdmin)
