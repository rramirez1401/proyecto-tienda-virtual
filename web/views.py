from django.shortcuts import render
from .models import Flan
from django.views.generic import ListView, TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin



class HomeView(ListView):
    model = Flan
    template_name = "index.html"
    context_object_name = "flanes"

    def get_queryset(self):
        return Flan.objects.filter(is_private=False)
    

class WelcomeView(LoginRequiredMixin, ListView):
    model = Flan
    template_name = "welcome.html"
    context_object_name = "flanes"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["flanes_publicos"] = Flan.objects.filter(is_private=False)
        context["flanes_privados"] = Flan.objects.filter(is_private=True)
        return context



class AboutView(TemplateView):
    template_name = "about.html"



class FlanDetailView(DetailView):
    model = Flan
    template_name = "detail.html"
    context_object_name = "flan"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    @staticmethod
    def group_queryset(queryset, n):
        return [list(queryset[i:i + n]) for i in range(0, len(queryset), n)]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated:
            relacionados = Flan.objects.exclude(pk=self.object.pk)
        else:
            relacionados = Flan.objects.filter(is_private=False).exclude(pk=self.object.pk)
        context['relacionados_grupos'] = self.group_queryset(relacionados, 4)
        return context



from django.http import HttpResponse
from django.db import connection

def test_db_connection(request):
    try:
        # Ejecuta una consulta simple
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1;")
            row = cursor.fetchone()
        return HttpResponse(f"✅ DB OK! Resultado de SELECT 1: {row[0]}")
    except Exception as e:
        return HttpResponse(f"❌ Error DB: {e}")
    


from django.core.management import call_command

def run_migrations(request):
    try:
        call_command("migrate", interactive=False)
        return HttpResponse("✅ Migraciones ejecutadas correctamente")
    except Exception as e:
        return HttpResponse(f"❌ Error: {e}")
    


def load_fixtures(request):
    try:
        call_command("loaddata", "web/fixtures/flanes.json")
        return HttpResponse("✅ Fixture cargado")
    except Exception as e:
        return HttpResponse(f"❌ Error: {e}")