from django.shortcuts import render, redirect
from .models import Flan
from django.contrib.auth.decorators import login_required
from .forms import ContactFormModelForm
from django.contrib import messages


def home(request):
    flanes = Flan.objects.filter(is_private=False)
    return render(request, "index.html", {"flanes": flanes})

@login_required
def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, "welcome.html", {"flanes_privados":flanes_privados})


def about(request):
    return render(request, "about.html", {})

def contact(request):
    if request.method == "POST":
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Gracias por tu mensaje. ¡Nos pondremos en contacto contigo pronto!")
        else:
            messages.error(request, "Por favor corrige los errores del formulario.")
    return redirect(request.META.get("HTTP_REFERER", "/"))

