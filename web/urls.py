
from django.urls import path
from .views import home, about, welcome

urlpatterns = [
    path("", home, name="home"),
    path("acerca/", about, name="about"),
    path("bienvenido/", welcome, name="welcome"),
]
