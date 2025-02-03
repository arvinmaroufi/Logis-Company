from django.contrib import admin
from . import models


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['author', 'short_title', 'created_at', 'status']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['status']
    search_fields = ['title']

    def short_title(self, obj):
        if len(obj.title) > 20:
            return obj.title[:20] + '...'
        return obj.title

    short_title.short_description = 'title'
