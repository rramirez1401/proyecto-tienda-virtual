from django.shortcuts import render, redirect
from .models import Flan, ContactForm
from django.contrib.auth.decorators import login_required
from .forms import ContactFormForm
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
        form = ContactFormForm(request.POST)
        if form.is_valid():
            # Extraigo los datos del formulario
            nombre = form.cleaned_data["customer_name"]
            correo = form.cleaned_data["customer_email"]
            mensaje = form.cleaned_data["message"]
            
            # Creo una instancia de ContactForm para pasarle los datos del formulario
            contacto = ContactForm(customer_name = nombre, customer_email=correo, message=mensaje)
            contacto.save()

            messages.success(request, "Gracias por tu mensaje!!! Nos pondremos en contacto contigo lo antes posible")

            return redirect("success")
    
    else:
        form = ContactFormForm()
    
    return render(request, "contact.html", {"form":form})