from django.db import models
from django.db.models import Q

from core.models import BaseModel
from core.utils.upload import UploadToPath

from .product import Product


class ProductImage(BaseModel):
    """
    تصاویر محصول
    """

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="محصول",
    )

    image = models.ImageField(
        upload_to=UploadToPath("products"),
        verbose_name="تصویر",
    )

    alt_text = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="متن جایگزین (SEO)",
    )

    sort_order = models.PositiveIntegerField(
        default=0,
        verbose_name="ترتیب نمایش",
    )

    is_cover = models.BooleanField(
        default=False,
        verbose_name="تصویر اصلی",
    )

    class Meta:

        ordering = (
            "sort_order",
            "id",
        )

        constraints = [

            models.UniqueConstraint(
                fields=["product"],
                condition=Q(is_cover=True),
                name="unique_cover_image_per_product",
            )

        ]

        verbose_name = "تصویر محصول"

        verbose_name_plural = "تصاویر محصول"

    def __str__(self):

        return f"{self.product.name} - Image #{self.pk}"

