# این همون لینک تیبل هست که مدل واریانت رو به مدل aterebute value وصل میکنه

from django.db import models

from core.models import BaseModel

from .variant import Variant
from .attribute_value import AttributeValue

class VariantAttribute(BaseModel):
    """
    Variant Attribute Value
    """

    variant = models.ForeignKey(
        Variant,
        on_delete=models.CASCADE,
        related_name="variant_attributes",
        verbose_name="واریانت",
    )

    attribute_value = models.ForeignKey(
        AttributeValue,
        on_delete=models.PROTECT,
        related_name="variant_attributes",
        verbose_name="مقدار ویژگی",
    )

    class Meta:

        ordering = [
            "variant",
        ]

        constraints = [

            models.UniqueConstraint(
                fields=[
                    "variant",
                    "attribute_value",
                ],
                name="unique_variant_attribute",
            )

        ]

        verbose_name = "ویژگی واریانت"

        verbose_name_plural = "ویژگی‌های واریانت"

    def __str__(self):

        return f"{self.variant} - {self.attribute_value}"