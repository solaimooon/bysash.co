from django.urls import path,include
from django.conf import settings
from .views import *

urlpatterns = [

path("", HomeView.as_view(), name="home"),
path("shop/",ProductListView.as_view(),name="shop",),
# path("category/<str:slug>/", ,name='category'),
# path("brand/<str:slug>/", ,name='brand'),
# path("product/<str:slug>/", ,name='product'),
]