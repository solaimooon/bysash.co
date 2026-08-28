
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect

from ai.models import AIImagePrompt
from store.models import ProductImage

from .services.product_image_service import ProductImageAIService


def edit_product_image_with_ai(request, image_id):

    product_image = get_object_or_404(
        ProductImage,
        pk=image_id,
    )

    try:

        # دریافت پرامپت فعال
        active_prompt = AIImagePrompt.objects.filter(
            is_active=True
        ).first()

        if not active_prompt:
            messages.error(
                request,
                "هیچ پرامپت فعالی برای ویرایش تصویر تنظیم نشده است.",
            )

            return redirect(
                "admin:store_product_change",
                product_image.product.id,
            )

        service = ProductImageAIService()

        new_image = service.edit_product_image(
            product_image=product_image,
            prompt=active_prompt.prompt,
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


