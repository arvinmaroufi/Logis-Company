from django.contrib import admin
from . import models


class ProjectImageAdmin(admin.TabularInline):
    model = models.ProjectImage


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageAdmin]
    list_display = ['title', 'created_at']
    search_fields = ['title']
