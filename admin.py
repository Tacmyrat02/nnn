from django.contrib import admin
from .models import VPNConfig

@admin.register(VPNConfig)
class VPNConfigAdmin(admin.ModelAdmin):
    list_display = ('name', 'token', 'created_at')
