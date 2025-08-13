
from django.urls import path
from .views import HomeView, AboutView, WelcomeView, FlanDetailView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("acerca/", AboutView.as_view(), name="about"),
    path("bienvenido/", WelcomeView.as_view(), name="welcome"),
    path("producto/<slug:slug>/", FlanDetailView.as_view(), name="detalle"),
]
