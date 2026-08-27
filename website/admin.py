from django.contrib import admin

from django.contrib import admin

from .models import HeroSlider


@admin.register(HeroSlider)
class HeroSliderAdmin(admin.ModelAdmin):

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
# Register your models here.
