from django.contrib import admin

from .models import AIImagePrompt
from unfold.admin import ModelAdmin

@admin.register(AIImagePrompt)
class AIImagePromptAdmin(ModelAdmin):

    list_display = (
        "id",
        "name",
        "prompt_preview",
        "is_active",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "prompt",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    @admin.display(description="پرامپت")
    def prompt_preview(self, obj):
        return obj.prompt[:80]

    def save_model(self, request, obj, form, change):

        if obj.is_active:
            AIImagePrompt.objects.exclude(
                pk=obj.pk
            ).update(
                is_active=False
            )

        super().save_model(
            request,
            obj,
            form,
            change,
        )

    def has_add_permission(self, request):
        return True