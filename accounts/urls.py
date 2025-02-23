from django.contrib import admin
from django.urls import path, include
from accounts import views as account_views

urlpatterns = [

    path('signup/', account_views.signupView, name='signup'),
    path('login/', account_views.loginView, name='login'),
    path('logout/', account_views.logout_view, name='logout'),

]