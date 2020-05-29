from django.contrib import admin
from pages.models import Page


class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Page, PageAdmin)
