from django.db import models


class HeroSlider(models.Model):

    title_small = models.CharField(
        max_length=100,
        verbose_name="عنوان کوچک",
        blank=True,
    )

    title = models.CharField(
        max_length=255,
        verbose_name="عنوان اصلی",
    )

    description = models.TextField(
        verbose_name="توضیحات",
        blank=True,
    )

    button_text = models.CharField(
        max_length=100,
        verbose_name="متن دکمه",
        blank=True,
    )

    button_url = models.CharField(
        max_length=255,
        verbose_name="لینک دکمه",
        blank=True,
    )

    desktop_image = models.ImageField(
        upload_to="sliders/desktop/",
        verbose_name="تصویر دسکتاپ",
    )

    mobile_image = models.ImageField(
        upload_to="sliders/mobile/",
        verbose_name="تصویر موبایل",
        blank=True,
        null=True,
    )

    sort_order = models.PositiveIntegerField(
        default=0,
        verbose_name="ترتیب نمایش",
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ایجاد",
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="آخرین بروزرسانی",
    )

    class Meta:
        ordering = ["sort_order", "-created_at"]
        verbose_name = "اسلایدر"
        verbose_name_plural = "اسلایدرها"

    def __str__(self):
        return self.title