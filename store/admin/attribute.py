from django.contrib import admin

from store.models import Attribute


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "attribute_type",
        "sort_order",
        "is_active",
    )

    list_editable = (
        "attribute_type",
        "sort_order",
        "is_active",
    )

    list_filter = (
        "attribute_type",
        "is_active",
    )

    search_fields = (
        "name",
    )

    ordering = (
        "sort_order",
        "name",
    )

    fieldsets = (
        (
            "اطلاعات ویژگی",
            {
                "fields": (
                    "name",
                    "attribute_type",
                )
            },
        ),
        (
            "تنظیمات نمایش",
            {
                "fields": (
                    "sort_order",
                    "is_active",
                )
            },
        ),
    )