from django.shortcuts import render, redirect
from .models import Flan
from django.contrib.auth.decorators import login_required
from .forms import ContactFormModelForm
from django.contrib import messages



def home(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, "index.html", {"flanes":flanes_publicos})

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
            messages.success(request, "Gracias por tu mensaje!!! Nos pondremos en contacto contigo lo antes posible")
            return redirect("success")
    
    else:
        form = ContactFormModelForm()
    
    return render(request, "contact.html", {"form":form})