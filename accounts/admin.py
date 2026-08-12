from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class MyUserAdmin(UserAdmin):

    ordering = ("id",)

    list_display = (
        "id",
        "phone_number",
        "first_name",
        "last_name",
        "user_type",
        "is_active",
        "is_staff",
    )

    fieldsets = (
        (None, {
            "fields": (
                "phone_number",
                "password",
            )
        }),

        ("اطلاعات شخصی", {
            "fields": (
                "first_name",
                "last_name",
                "email",
            )
        }),

        ("سطح دسترسی", {
            "fields": (
                "user_type",
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            )
        }),

        ("وضعیت", {
            "fields": (
                "is_phone_verified",
            )
        }),

        ("تاریخ‌ها", {
            "fields": (
                "last_login",
                "date_joined",
            )
        }),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "phone_number",
                    "password1",
                    "password2",
                    "user_type",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )