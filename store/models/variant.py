from django.db import models

from core.models import BaseModel

from .product import Product


class Variant(BaseModel):
    """
    Product Variant
    Example:
        Black / XL
        White / L
    """

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="variants",
        verbose_name="محصول",
    )

    sku = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="SKU",
    )

    barcode = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="بارکد",
    )

    price = models.DecimalField(
        max_digits=12,
        decimal_places=0,
        verbose_name="قیمت",
    )

    discount_price = models.DecimalField(
        max_digits=12,
        decimal_places=0,
        blank=True,
        null=True,
        verbose_name="قیمت با تخفیف",
    )

    stock = models.PositiveIntegerField(
        default=0,
        verbose_name="موجودی",
    )

    weight = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="وزن (گرم)",
    )

    is_default = models.BooleanField(
        default=False,
        verbose_name="واریانت پیش‌فرض",
    )

    class Meta:
        ordering = [
            "product",
            "-is_default",
            "id",
        ]

        verbose_name = "واریانت"

        verbose_name_plural = "واریانت‌ها"

    def __str__(self):
        return f"{self.product.name} ({self.sku})"

