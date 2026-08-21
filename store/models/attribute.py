from django.db import models

from core.models import BaseModel
from store.choices import AttributeType

class Attribute(BaseModel):
    """
    Product Attribute
    Example:
        Color
        Size
        Material
    """

    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="نام ویژگی",
    )

    attribute_type = models.CharField(
        max_length=20,
        choices=AttributeType.choices,
        default=AttributeType.OTHER,
        verbose_name="نوع ویژگی",
    )


    sort_order = models.PositiveIntegerField(
        default=0,
        verbose_name="ترتیب نمایش",
    )

    class Meta:
        ordering = (
            "sort_order",
            "name",
        )

        verbose_name = "ویژگی"

        verbose_name_plural = "ویژگی‌ها"

    def __str__(self):
        return self.name