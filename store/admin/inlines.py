from django.contrib import admin

from store.models import ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage

    extra = 1

    fields = (
        "image",
        "alt_text",
        "sort_order",
        "is_cover",
    )

    ordering = (
        "sort_order",
    )



from store.models import Variant


class VariantInline(admin.TabularInline):

    model = Variant

    extra = 1

    fields = (
        "sku",
        "price",
        "discount_price",
        "stock",
        "is_default",
        "is_active",
    )

    show_change_link = True



from store.models import VariantAttribute


class VariantAttributeInline(admin.TabularInline):
    model = VariantAttribute

    extra = 1

    autocomplete_fields = (
        "attribute_value",
    )