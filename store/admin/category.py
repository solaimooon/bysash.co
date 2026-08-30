from django.contrib import admin

from mptt.admin import DraggableMPTTAdmin
from unfold.admin import ModelAdmin

from store.models import Category


@admin.register(Category)
class CategoryAdmin(ModelAdmin, DraggableMPTTAdmin):

    list_display = (
        "tree_actions",
        "indented_title",
        "is_active",
        "sort_order",
    )

    list_display_links = (
        "indented_title",
    )

    search_fields = (
        "name",
        "slug",
    )

    list_filter = (
        "is_active",
    )

    prepopulated_fields = {}

    mptt_level_indent = 25