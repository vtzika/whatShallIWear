from django.contrib import admin
from sources.models import Source


class SourceAdmin(admin.ModelAdmin):
    list_display = ('source_url', 'gender', 'place')

admin.site.register(Source, SourceAdmin)
