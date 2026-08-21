from django.db import models

from core.models import BaseModel
from core.mixins.slug import SlugMixin

from .brand import Brand
from .category import Category

from store.choices import ProductStatus
from django_ckeditor_5.fields import CKEditor5Field

class Product(SlugMixin, BaseModel):
    """
    Product
    """

    name = models.CharField(
        max_length=255,
        verbose_name="نام محصول",
    )

    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
        verbose_name="اسلاگ",
        help_text="این فیلد به صورت هوشمند توسط سیستم ثبت میشود(لازم نیست مقداری وارد نمایید)"
    )

    categories = models.ManyToManyField(
        Category,
        related_name="products",
        verbose_name="دسته بندی ها",
    )

    brand = models.ForeignKey(
        Brand,
        on_delete=models.SET_NULL,
        related_name="products",
        blank=True,
        null=True,
        verbose_name="برند",
    )

    short_description = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="توضیح کوتاه",
    )

    description = CKEditor5Field('Text', config_name='extends')

    status = models.CharField(
        max_length=20,
        choices=ProductStatus.choices,
        default=ProductStatus.DRAFT,
        verbose_name="وضعیت",
    )

    is_featured = models.BooleanField(
        default=False,
        verbose_name="محصول ویژه",
    )

    class Meta:

        ordering = [
            "-created_at",
        ]

        verbose_name = "محصول"

        verbose_name_plural = "محصولات"

    def __str__(self):

        return self.name

    @property
    def cover_image(self):
        return self.images.filter(is_cover=True).first()

    @property
    def default_variant(self):
        return self.variants.filter(is_default=True).first()

    @property
    def price(self):
        if self.default_variant:
            return self.default_variant.price
        return None

    @property
    def discount_price(self):
        if self.default_variant:
            return self.default_variant.discount_price
        return None
