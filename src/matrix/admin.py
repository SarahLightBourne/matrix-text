from . import models
from django.contrib import admin


class LabelInline(admin.TabularInline):
    model = models.Label
    classes = ['collapse']
    extra = 1


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'active']
    search_fields = ['name']
    list_filter = ['active']
    inlines = [LabelInline]


@admin.register(models.Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ['text', 'active', 'collection']
    search_fields = ['text']
    list_filter = ['active']
