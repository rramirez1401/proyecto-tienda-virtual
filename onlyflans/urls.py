
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("web.urls")),
    path("usuarios/", include("users.urls")),
]

# En producción con Gunicorn (Render free) no se sirve MEDIA por defecto.
# Esto permite que se resuelva /media/... usando la misma vista de archivos estáticos.
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)