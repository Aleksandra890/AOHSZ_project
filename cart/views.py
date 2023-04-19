from django.shortcuts import render, redirect
from .models import Cart
from django.contrib.auth.models import User

def Cartochka(request):

    if request.user.is_superuser:
        cart = Cart.objects.all()
        user = User.objects.all()
         
    else:
        cart = Cart.objects.all().filter(catProf=request.user.username)
        user = User.objects.all()
    return render(request, 'cart/Cart.html',{'cart':cart })

def cartclear(request):
    user=request.user.username
    Cart.objects.filter(catProf=user).all().delete()
    return redirect('../cart/cartochka')










