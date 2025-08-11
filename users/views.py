from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import RegisterForm

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