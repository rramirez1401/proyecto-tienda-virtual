
from django.urls import path
from .views import HomeView, AboutView, WelcomeView, FlanDetailView, test_db_connection, load_fixtures, run_migrations

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("acerca/", AboutView.as_view(), name="about"),
    path("bienvenido/", WelcomeView.as_view(), name="welcome"),
    path("producto/<slug:slug>/", FlanDetailView.as_view(), name="detalle"),

    path("test-db/", test_db_connection, name="test-db"),
    path("run-loaddata/", load_fixtures, name="run-loaddata"),
    path("run-migrations/", run_migrations, name="run-migrations"),

]
