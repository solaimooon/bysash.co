from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect

from store.models import ProductImage

from .services.product_image_service import (
    ProductImageAIService,
)


def edit_product_image_with_ai(request, image_id):

    product_image = get_object_or_404(
        ProductImage,
        pk=image_id,
    )

    prompt = """
    Edit this product photo for a professional fashion e-commerce store.

    Keep the clothing product itself unchanged.

    Remove the existing background and replace it with
    a clean, premium, minimal studio background.

    Improve lighting and image quality while keeping
    the original product appearance realistic.

    Do not change the color, shape, design, or details
    of the clothing.
    """

    try:

        service = ProductImageAIService()

        new_image = service.edit_product_image(
            product_image=product_image,
            prompt=prompt,
        )

        messages.success(
            request,
            "تصویر با موفقیت توسط هوش مصنوعی ویرایش و ذخیره شد.",
        )

        return redirect(
            "admin:store_product_change",
            product_image.product.id,
        )

    except Exception as e:

        messages.error(
            request,
            f"ویرایش تصویر با هوش مصنوعی انجام نشد: {str(e)}",
        )

        return redirect(
            "admin:store_product_change",
            product_image.product.id,
        )