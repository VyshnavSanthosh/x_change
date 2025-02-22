from django.shortcuts import render, redirect
from products.models import Product

def index(request):
    products = Product.objects.all()
    return render(request,'home.html', {'products': products})

