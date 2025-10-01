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


