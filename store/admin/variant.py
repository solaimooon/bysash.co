from django.contrib import admin
from django.utils.html import format_html

from store.models import Variant
from .inlines import VariantAttributeInline


@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):

    list_display = (
        "sku",
        "product",
        "attributes_display",
        "price",
        "stock",
        "is_default",
        "is_active",
        "created_at",
    )

    list_display_links = (
        "sku",
    )

    search_fields = (
        "sku",
        "product__name",
    )

    list_filter = (
        "is_default",
        "is_active",
        "product__brand",
        "product__categories",
    )

    autocomplete_fields = (
        "product",
    )

    list_select_related = (
        "product",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = (
        "-created_at",
    )

    list_per_page = 25

    date_hierarchy = "created_at"

    save_on_top = True

    save_as = True

    save_as_continue = False

    inlines = (
        VariantAttributeInline,
    )

    fieldsets = (
        (
            "اطلاعات اصلی",
            {
                "fields": (
                    "product",
                    "sku",
                )
            },
        ),
        (
            "قیمت",
            {
                "fields": (
                    "price",
                    "discount_price",
                )
            },
        ),
        (
            "انبار",
            {
                "fields": (
                    "stock",
                )
            },
        ),
        (
            "تنظیمات",
            {
                "fields": (
                    "is_default",
                    "is_active",
                )
            },
        ),
        (
            "اطلاعات ثبت",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related(
            "product",
        ).prefetch_related(
            "variant_attributes__attribute_value__attribute",
        )

    @admin.display(description="ویژگی‌ها")
    def attributes_display(self, obj):
        values = obj.variant_attributes.all()

        if not values.exists():
            return "-"

        return format_html(
            "<br>".join(
                "{}: <strong>{}</strong>".format(
                    item.attribute_value.attribute.name,
                    item.attribute_value.value,
                )
                for item in values
            )
        )