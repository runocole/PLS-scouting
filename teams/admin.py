from django.contrib import admin
from .models import Team
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')
    search_fields = ('name',)

