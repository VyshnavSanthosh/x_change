from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Product


class SellProduct(forms.ModelForm):
    class  Meta:
        model = Product
        fields = ['name', 'price', 'description', 'months_used', 'image']


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username','email','password1','password2') 