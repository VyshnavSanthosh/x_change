from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.

def signupView(request):
    if request.method ==  'POST':
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "You have been successfully registered.")
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def loginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'] , password=form.cleaned_data['password'])
            login(request, user)
            messages.success(request, "You have been successfully logged in.")
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)  # Destroy user session
    return redirect('home')  # Redirect to homepage/login