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
        form = LoginForm(request, data=request.POST)  # Pass request for auth
        if form.is_valid():
            user = form.get_user()  # Built-in method to get authenticated user
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect('home')
        else:
            # Form errors are already included in the template
            print("Login failed.")
            print(form.get_user())
            print(request.POST)
            messages.error(request, "Login failed. Fix errors below.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)  # Destroy user session
    print("logged out successfully.")
    return redirect('home')  # Redirect to homepage/login