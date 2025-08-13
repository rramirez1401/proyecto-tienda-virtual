
from django.urls import path
from .views import RegisterView, LogoutGetView, CustomLoginView, contact_view


urlpatterns = [
    path("registro/", RegisterView.as_view(),name="signup"),
    path("iniciar_sesion/", CustomLoginView.as_view(),name="login"),
    path("salir/", LogoutGetView.as_view(), name="logout"),
    path("contacto/", contact_view, name="contact"),
]
