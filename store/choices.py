from django.db import models


class ProductStatus(models.TextChoices):

    DRAFT = "draft", "پیش نویس"

    PUBLISHED = "published", "منتشر شده"

    ARCHIVED = "archived", "آرشیو شده"