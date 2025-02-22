from itertools import product
from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.products_page, name='products_page' ),
    path('product/<int:pk>/',views.product_detail,name = 'product_detail'),
    path('sell/',views.sell_page,name = 'sell')
]