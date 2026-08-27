from django.urls import path

from .views import edit_product_image_with_ai


app_name = "ai"


urlpatterns = [
    path(
        "product-image/<int:image_id>/edit/",
        edit_product_image_with_ai,
        name="edit_product_image",
    ),
]