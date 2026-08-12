from django.db import models

from core.models import BaseModel

from .attribute import Attribute


class AttributeValue(BaseModel):
    """
    Product Attribute Value
    Example:
        Color -> Red
        Size -> XL
    """

    attribute = models.ForeignKey(
        Attribute,
        on_delete=models.CASCADE,
        related_name="values",
        verbose_name="ویژگی",
    )

    value = models.CharField(
        max_length=100,
        verbose_name="مقدار",
    )

    sort_order = models.PositiveIntegerField(
        default=0,
        verbose_name="ترتیب نمایش",
    )

    class Meta:
        ordering = (
            "attribute",
            "sort_order",
            "value",
        )

        constraints = [
            models.UniqueConstraint(
                fields=["attribute", "value"],
                name="unique_attribute_value",
            )
        ]

        verbose_name = "مقدار ویژگی"

        verbose_name_plural = "مقادیر ویژگی"

    def __str__(self):
        return f"{self.attribute.name} : {self.value}"