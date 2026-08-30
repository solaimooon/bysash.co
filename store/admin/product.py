from django.contrib import admin
from django.utils.html import format_html

from unfold.admin import ModelAdmin

from store.models import Product

from .inlines import (
    ProductImageInline,
    VariantInline,
)


@admin.register(Product)
class ProductAdmin(ModelAdmin):

    list_display = (
        "name",
        "brand",
        "status_badge",
        "is_active",
        "variant_count",
        "cover_image_preview",
        "created_at",
    )

    @admin.display(description="وضعیت")
    def status_badge(self, obj):
        return obj.status

    @admin.display(description="تعداد واریانت")
    def variant_count(self, obj):
        return obj.variants.count()

    @admin.display(description="تصویر")
    def cover_image_preview(self, obj):
        cover = obj.images.filter(is_cover=True).first()

        if cover and cover.image:
            return format_html(
                '<img src="{}" width="60" height="60" '
                'style="border-radius:8px; object-fit:cover;" />',
                cover.image.url,
            )

        return "-"

    search_fields = (
        "name",
        "slug",
        "brand__name",
    )

    list_filter = (
        "status",
        "is_active",
        "brand",
        "categories",
    )

    autocomplete_fields = (
        "brand",
        "categories",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    list_select_related = (
        "brand",
    )

    inlines = (
        ProductImageInline,
        VariantInline,
    )

    fieldsets = (
        (
            "اطلاعات اصلی",
            {
                "fields": (
                    "name",
                    "slug",
                    "brand",
                    "categories",
                ),
            },
        ),
        (
            "توضیحات",
            {
                "fields": (
                    "short_description",
                    "description",
                ),
            },
        ),
        (
            "وضعیت",
            {
                "fields": (
                    "status",
                    "is_active",
                    "is_featured",
                ),
            },
        ),
        (
            "اطلاعات سیستم",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                ),
            },
        ),
    )

    ordering = (
        "-created_at",
    )

    save_as = True
    save_on_top = True
    save_as_continue = False