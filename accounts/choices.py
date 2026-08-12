from django.db import models


class UserType(models.TextChoices):
    CUSTOMER = "customer", "مشتری"
    STAFF = "staff", "کارمند"
    ADMIN = "admin", "مدیر"