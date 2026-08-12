from django.db import models

from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey

from core.models import BaseModel
from core.mixins.slug import SlugMixin
from core.utils.upload import UploadToPath


class Category(SlugMixin, MPTTModel, BaseModel):
    """
    Product Category
    """

    name = models.CharField(
        max_length=150,
        verbose_name="نام دسته‌بندی",
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

    image = models.ImageField(
        upload_to=UploadToPath("category"),
        blank=True,
        null=True,
    )

    parent = TreeForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="children",
        blank=True,
        null=True,
        verbose_name="دسته‌بندی والد",
    )

    sort_order = models.PositiveIntegerField(
        default=0,
        verbose_name="ترتیب نمایش",
    )

    class MPTTMeta:
        order_insertion_by = [
            "sort_order",
            "name",
        ]

    class Meta:
        ordering = [
            "sort_order",
            "name",
        ]
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"

    def __str__(self):
        return self.name