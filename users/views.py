from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from .forms import RegisterForm
from django.views import View
from django.contrib.auth.views import LoginView

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Opcional: loguea automáticamente
            messages.success(request, '¡Registro exitoso! Bienvenido.')
            return redirect('home')  # Cambia por tu URL deseada
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = "welcome.html"
    redirect_authenticated_user = True
    def form_valid(self, form):
        messages.success(self.request, "Sesión iniciada correctamente") 
        return super().form_valid(form)

class LogoutGetView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "Has cerrado sesión correctamente.")
        return redirect('home')