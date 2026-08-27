from django.contrib import admin

from store.models import ProductImage
from django.utils.html import format_html

from django.contrib import admin
from django.utils.html import format_html

from store.models import ProductImage
from django.urls import reverse

from django.contrib import admin
from django.utils.html import format_html

from store.models import ProductImage


class ProductImageInline(admin.TabularInline):

    model = ProductImage

    extra = 1

    fields = (
        "image",
        "alt_text",
        "sort_order",
        "is_cover",
        "ai_edit_button",
    )

    readonly_fields = (
        "ai_edit_button",
    )

    ordering = (
        "sort_order",
    )

    @admin.display(description="هوش مصنوعی")
    def ai_edit_button(self, obj):
        if not obj.pk:
            return "-"

        url = reverse(
            "ai:edit_product_image",
            args=[obj.pk],
        )

        return format_html(
            '<a class="button" href="{}">'
            '🤖 ویرایش با هوش مصنوعی'
            '</a>',
            url,
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