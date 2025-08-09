
from django.urls import path
from .views import home, about, welcome, contact
from django.views.generic import TemplateView

urlpatterns = [
    path("", home, name="home"),
    path("acerca/", about, name="about"),
    path("bienvenido/", welcome, name="welcome"),
    path("contacto/", contact, name="contact"),
    path("exito/", TemplateView.as_view(template_name="exito.html"), name="success"),
]
