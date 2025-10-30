from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required



@login_required
def add_to_cart(request):
    flan_id = str(request.POST.get('flan_id'))
    quantity = int(request.POST.get('quantity', 1))

    cart = request


@login_required
def checkout_view(request):

    cart = request.session.get()
