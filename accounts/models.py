from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.contrib.auth.base_user import BaseUserManager
from django.core.validators import RegexValidator
from .choices import UserType
from core.models import BaseModel

# vallidate the phonenumber 
phone_regex = RegexValidator(
    regex=r"^09\d{9}$",
    message="شماره موبایل معتبر نیست."
)


class MyUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, phone_number, password=None, **extra_fields):

        if not phone_number:
            raise ValueError("Phone number is required.")

        user = self.model(
            phone_number=phone_number,
            **extra_fields
        )

        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("user_type", "admin")
        extra_fields.setdefault("is_phone_verified", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(
            phone_number,
            password,
            **extra_fields
        )

class UserType(models.TextChoices):
    CUSTOMER = "customer", "مشتری"
    STAFF = "staff", "کارمند"
    ADMIN = "admin", "مدیر"


class User(AbstractUser,BaseModel):
    username = None

    phone_number = models.CharField(
        max_length=11,
        unique=True,
        verbose_name="شماره موبایل",
        validators=[phone_regex],
    )

    email = models.EmailField(
        blank=True,
    )

    user_type = models.CharField(
        max_length=20,
        choices=UserType.choices,
        default=UserType.CUSTOMER
    )

    is_phone_verified = models.BooleanField(
        default=False
    )

    USERNAME_FIELD = "phone_number"

    REQUIRED_FIELDS = []
    
    objects = MyUserManager()

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"

    def __str__(self):
        return self.phone_number
    
    
    