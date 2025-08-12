
from django.urls import path
from .views import register, LogoutGetView, CustomLoginView


urlpatterns = [
    path("registro", register,name="signup"),
    path("iniciar_sesion/", CustomLoginView.as_view(),name="login"),
    path("salir/", LogoutGetView.as_view(), name="logout"),
]
