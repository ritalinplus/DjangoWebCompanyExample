from django.contrib import admin
from services.models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')