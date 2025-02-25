from django.http import request
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Product
from .forms import SellProduct
# Create your views here.
def products_page(request):
    products = Product.objects.all()
    print(products)
    return render(request,'products.html', {'products':products})

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request,'product_details.html', {'product':product})

def sell_page(request):
    if request.method == 'POST':
        form = SellProduct(request.POST, request.FILES)
        if form.is_valid():
            sell = form.save(commit=False)
            sell.user = request.user
            sell.save()
            print("successfully sold", sell.user)
            return redirect('home')
        else:
            print("Form errors:", form.errors)  # Print any form validation errors
    else:
        form = SellProduct()
    return render(request, 'sell_page.html', {'form': form})