from django.db import models

from core.models import BaseModel
from core.mixins.slug import SlugMixin
from core.utils.upload import UploadToPath


class Brand(SlugMixin, BaseModel):
    """
    Product Brand
    """

    name = models.CharField(
        max_length=150,
        verbose_name="نام برند",
    )

    slug = models.SlugField(
        max_length=200,
        unique=True,
        blank=True,
        verbose_name="اسلاگ",
        help_text="این فیلد به صورت هوشمند توسط سیستم ثبت میشود(لازم نیست مقداری وارد نمایید)"
    )

    description = models.TextField(
        blank=True,
        verbose_name="توضیحات",
    )

    logo = models.ImageField(
        upload_to=UploadToPath("brand"),
        blank=True,
        null=True,
        verbose_name="لوگو",
    )

    is_featured = models.BooleanField(
        default=False,
        verbose_name="برند ویژه",
    )

    class Meta:
        ordering = ["name"]

        verbose_name = "برند"

        verbose_name_plural = "برندها"

    def __str__(self):
        return self.name