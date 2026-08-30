from unfold.admin import ModelAdmin

from django.contrib import admin

from .models import HeroSlider


@admin.register(HeroSlider)
class HeroSliderAdmin(ModelAdmin):

    list_display = (
        "title",
        "sort_order",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "title",
        "description",
    )

    list_editable = (
        "sort_order",
        "is_active",
    )

    ordering = (
        "sort_order",
        "-created_at",
    )

from django.contrib import admin

from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(ModelAdmin):

    list_display = (
        "full_name",
        "phone",
        "email",
        "subject",
        "created_at",
        "is_read",
    )

    list_filter = (
        "subject",
        "is_read",
        "created_at",
    )

    search_fields = (
        "full_name",
        "phone",
        "email",
        "message",
    )

    readonly_fields = (
        "created_at",
    )

    list_editable = (
        "is_read",
    )

    ordering = (
        "-created_at",
    )

    fieldsets = (
        (
            "اطلاعات تماس",
            {
                "fields": (
                    "full_name",
                    "phone",
                    "email",
                ),
            },
        ),
        (
            "اطلاعات درخواست",
            {
                "fields": (
                    "subject",
                    "message",
                ),
            },
        ),
        (
            "وضعیت پیام",
            {
                "fields": (
                    "is_read",
                    "created_at",
                ),
            },
        ),
    )
