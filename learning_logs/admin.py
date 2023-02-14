from django.contrib import admin

from . import models


@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ["title", "public", "date_created", "owner"]
    list_filter = ["public", "date_created", "owner"]
    search_fields = ["title"]


@admin.register(models.Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ["topic", "content", "date_created"]
    list_filter = ["topic", "date_created"]
