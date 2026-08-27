from django.urls import path,include
from django.conf import settings
from .views import *

app_name='store'

urlpatterns = [
path("",ProductListView.as_view(),name="shop",),
    path(
        "product/<str:slug>/",
        ProductDetailView.as_view(),
        name="product-detail",
    ),
]