from django.urls import path,include
from django.conf import settings
from .views import *

app_name='website'

urlpatterns = [
path("", HomeView.as_view(), name="home"),
path("about/", AboutVIEW.as_view(), name="about"),
path("contact",ContactUSView.as_view(), name="contact"),
]