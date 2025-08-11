
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from .views import register

urlpatterns = [
    path("registro", register,name="signup"),
    path("iniciar_sesion/", LoginView.as_view(template_name="login.html"),name="login"),
    path("salir/", LogoutView.as_view(next_page="home"),name="logout"),
]
