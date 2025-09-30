from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from .forms import RegisterForm, ContactFormModelForm
from django.views import View
from django.contrib.auth.views import LoginView
from users.forms import CustomAuthenticationForm
from django.views.generic import FormView, View
from django.urls import reverse_lazy

## REGISTRO
class RegisterView(FormView):
    template_name = "modals/modal_register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("welcome")


    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request,"¡Registro exitoso! ¡Ya puedes ver nuestros productos premium!")
        return super().form_valid(form)

    def form_invalid(self, form):
        # Renderiza la página principal con el formulario con errores
        from django.contrib.auth.forms import AuthenticationForm
        from users.forms import ContactFormModelForm
        return render(self.request, "index.html", {
            "register_form": form,
            "login_form": AuthenticationForm(),
            "contact_form": ContactFormModelForm(),
        })

## LOGIN
class CustomLoginView(LoginView):
    template_name = "modals/modal_login.html"
    redirect_authenticated_user = True
    authentication_form = CustomAuthenticationForm


    def form_valid(self, form):
        messages.success(self.request, "Sesión iniciada correctamente")
        return super().form_valid(form)

    def form_invalid(self, form):
        from users.forms import RegisterForm, ContactFormModelForm
        # Renderiza la página principal y mantiene la URL original
        response = render(self.request, "index.html", {
            "login_form": form,
            "register_form": RegisterForm(),
            "contact_form": ContactFormModelForm(),
        })
        response.status_code = 200
        return response

    def get_success_url(self):
        return reverse_lazy("welcome")


## LOGOUT
# modificacion para no requerir el form en template por problemas con la actualizacion
# del csrf token. No es necesrio el token para el logout
class LogoutGetView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "Has cerrado sesión. ¡Nos vemos pronto!")
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
