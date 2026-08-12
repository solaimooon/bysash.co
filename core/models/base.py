from django.db import models
from django_jalali.db import models as jmodels

class BaseModel(models.Model):

    created_at = jmodels.jDateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ایجاد"
    )

    updated_at = jmodels.jDateTimeField(
        auto_now=True,
        verbose_name="آخرین بروزرسانی"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    class Meta:
        abstract = True