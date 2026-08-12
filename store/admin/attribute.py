from django.contrib import admin

from store.models import Attribute


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "sort_order",
        "is_active",
    )

    list_editable = (
        "sort_order",
        "is_active",
    )

    search_fields = (
        "name",
    )

    ordering = (
        "sort_order",
        "name",
    )