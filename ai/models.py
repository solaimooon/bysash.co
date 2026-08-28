from django.db import models

class AIImagePrompt(models.Model):

    name=models.CharField(max_length=100,null=True,blank=True)

    prompt = models.TextField(
        verbose_name="پرامپت",
    )


    is_active = models.BooleanField(
        default=False,
        verbose_name="پرامپت فعال",
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
        verbose_name = "پرامپت تصویر AI"
        verbose_name_plural = "پرامپت‌های تصویر AI"

    def __str__(self):
        return self.prompt[:50]


