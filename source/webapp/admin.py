from django.contrib import admin

from source.webapp.models.comment import Comment
from source.webapp.models.tag import Tag
from source.webapp.models.task import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'created_at']
    list_display_links = ['id', 'title']
    list_filter = []
    search_fields = ['title', 'content']
    fields = ['title', 'author', 'content', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Task, TaskAdmin)
admin.site.register(Comment)
admin.site.register(Tag)