from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from .forms import RegisterForm, ContactFormModelForm
from django.views import View
from django.contrib.auth.views import LoginView
from django.views.generic import FormView, View
from django.urls import reverse_lazy

## REGISTRO
class RegisterView(FormView):
    template_name = "modals/modal_register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.save()
        messages.success(self.request,"¡Registro exitoso! ¡Ya puedes acceder y ver nuestros productos premium!")
        return super().form_valid(form)

## LOGIN
class CustomLoginView(LoginView):
    template_name = "modals/modal_login.html"
    redirect_authenticated_user = True

    def form_valid(self, form):
        messages.success(self.request, "Sesión iniciada correctamente")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("welcome")


## LOGOUT
# modificacion para no requerir el form en template por problemas con la actualizacion
# del csrf token. No es necesrio el token para el logout
class LogoutGetView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "Has cerrado sesión correctamente.")
        return redirect('home')


def contact_view(request):
    if request.method == "POST":
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Mensaje enviado correctamente!")
        else:
            messages.error(request, "Por favor corrige los errores en el formulario.")
        return redirect(request.META.get("HTTP_REFERER", "home"))
    return redirect("home")
