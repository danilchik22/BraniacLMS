from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from mainapp import models as mainapp_models


@admin.register(mainapp_models.News)
class NewsAdmin(admin.ModelAdmin):
    search_fields = ["title", "preambule", "body"]


@admin.register(mainapp_models.Lesson)
class Lesson(admin.ModelAdmin):
    list_display = ["course", "title", "description", "deleted"]
    ordering = ["-course"]
    list_filter = ["course", "title"]
    list_per_page = 5
    actions = ["mark_deleted", "mark_not_deleted"]

    def mark_deleted(self, request, queryset):
        queryset.update(deleted=True)

    mark_deleted.short_description = _("Mark deleted")

    def mark_not_deleted(self, request, queryset):
        queryset.update(deleted=False)

    mark_not_deleted.short_description = _("Mark not deleted")
