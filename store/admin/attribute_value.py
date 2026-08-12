from django.contrib import admin

from store.models import AttributeValue


@admin.register(AttributeValue)
class AttributeValueAdmin(admin.ModelAdmin):

    list_display = (
        "attribute",
        "value",
        "sort_order",
        "is_active",
    )

    list_filter = (
        "attribute",
        "is_active",
    )

    list_editable = (
        "sort_order",
        "is_active",
    )

    search_fields = (
        "value",
        "attribute__name",
    )

    ordering = (
        "attribute",
        "sort_order",
    )