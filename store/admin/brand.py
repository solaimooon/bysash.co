from django.contrib import admin
from unfold.admin import ModelAdmin
from store.models import Brand


@admin.register(Brand)
class BrandAdmin(ModelAdmin):

    list_display = (
        "name",
        "is_featured",
        "is_active",
    )

    list_filter = (
        "is_featured",
        "is_active",
    )

    search_fields = (
        "name",
        "slug",
    )

    ordering = (
        "name",
    )

    list_editable = (
        "is_featured",
        "is_active",
    )

    prepopulated_fields = {}