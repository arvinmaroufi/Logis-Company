from django.contrib import admin
from . import models


@admin.register(models.SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['address', 'phone', 'email']


@admin.register(models.ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['email', 'short_subject', 'short_message', 'date_send']

    def short_subject(self, obj):
        if len(obj.subject) > 20:
            return obj.subject[:20] + '...'
        return obj.subject

    short_subject.short_description = 'subject'

    def short_message(self, obj):
        if len(obj.message) > 20:
            return obj.message[:20] + '...'
        return obj.message

    short_message.short_description = 'message'


@admin.register(models.FAQ)
class FaqAdmin(admin.ModelAdmin):
    list_display = ['short_question', 'short_answer', 'created_at']

    def short_question(self, obj):
        if len(obj.question) > 30:
            return obj.question[:30] + '...'
        return obj.question
    short_question.short_description = 'question'

    def short_answer(self, obj):
        if len(obj.answer) > 30:
            return obj.answer[:30] + '...'
        return obj.answer
    short_answer.short_description = 'answer'


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_description']
    prepopulated_fields = {'slug': ('title',)}

    def short_description(self, obj):
        if len(obj.description) > 30:
            return obj.description[:30] + '...'
        return obj.description

    short_description.short_description = 'description'


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'profession', 'short_description', 'star']

    def short_description(self, obj):
        if len(obj.description) > 30:
            return obj.description[:30] + '...'
        return obj.description
    short_description.short_description = 'description'

