from django.core.files.base import ContentFile

from store.models import ProductImage

from .image_service import AIImageService


class ProductImageAIService:

    def __init__(self):

        self.ai_service = AIImageService()

    def edit_product_image(
        self,
        product_image,
        prompt,
        size="1024x1024",
    ):
        """
        Edit a ProductImage using AI
        and save the generated image
        as a new ProductImage.
        """

        image_bytes = self.ai_service.edit_django_image(
            django_image=product_image.image,
            prompt=prompt,
            size=size,
        )

        filename = (
            f"ai_{product_image.pk}_{product_image.product.slug}.png"
        )

        new_image = ProductImage(
            product=product_image.product,
            alt_text=product_image.alt_text,
            sort_order=product_image.sort_order + 1,
            is_cover=False,
        )

        new_image.image.save(
            filename,
            ContentFile(image_bytes),
            save=False,
        )

        new_image.save()

        return new_image