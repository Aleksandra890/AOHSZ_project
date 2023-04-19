from django.shortcuts import render, redirect
from .models import Product
from cart.models import Cart
from django.views.generic import DetailView


def products(request):
    object = Product.objects.all()
    return render(request, 'product/produkciya.html', {'object': object})

class ProdDetailView(DetailView):
    model = Product
    template_name = 'product/detailprod.html'
    context_object_name = 'post'

def prodv(request):
    object = Product.objects.order_by('metka')[:1]
    return render(request, 'product/prodvoen.html', {'object': object})

def prodg(request):
    object = Product.objects.order_by('-metka')[:4]
    return render(request, 'product/prodgrag.html', {'object': object})

def addincart(request):
  Cart.objects.create(
    catProf=request.user.username,
    nameCart=request.POST.get('postname'),
    textCart=request.POST.get('posttext1'),
    imageCart=request.POST.get('postimage')
    )
  return redirect('../cart/cartochka')

